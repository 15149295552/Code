import os
import platform
from typing import List

from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *
from selenium.webdriver import Chrome, ChromeOptions, ActionChains


class SeleniumHelper(Chrome):
    def __init__(self, wait=0, is_headless=False):
        options = ChromeOptions()
        options.add_argument("user-data-dir=" + self.__get_user_data_dir())  # 设置用户数据目录
        options.add_argument("--disable-blink-features=AutomationControlled")  # 禁用启用Blink运行时的功能
        options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 去除浏览器检测框
        options.add_argument('--disable-gpu')
        options.add_argument("window-size=1024,768")
        options.add_argument("--no-sandbox")
        if is_headless: options.add_argument('--headless')  # 无界面浏览器
        super().__init__(options=options)
        self.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                                Object.defineProperty(navigator, 'webdriver', {
                                    get: () => undefined
                                })
                """})  # 再次覆盖window.navigator.webdriver的值
        # 隐式等待
        self.implicitly_wait(wait)

    def __get_user_data_dir(self):
        os_name = platform.system()
        if 'Windows' == os_name:
            return r"C:\Users\%s\AppData\Local\Google\Chrome\User Data" % os.getlogin()
        if 'Linux' == os_name:
            return "/home/%s/.config/google-chrome" % os.getlogin()

    def scroll_by(self, x=0, y=0):
        """
            滑动滚轮
        :param x:水平方向
        :param y:垂直方向
        """
        self.execute_script("window.scrollBy(%s,%s)" % (x, y))

    def wait_presence_of_element(self, by, value, timeout=5, interval=0.5) -> WebElement:
        """
            等待单个元素出现
        :param by:查找依据
        :param value:查找元素
        :param timeout:等待最长时间
        :param interval:检测时间间隔
        :return:查找到的元素
        """
        return WebDriverWait(self, timeout, interval).until(presence_of_element_located((by, value)))

    def wait_leave_of_element(self, by, value, timeout=5, interval=0.5) -> bool:
        """
            等待单个元素离开
        :param by:查找依据
        :param value:查找元素
        :param timeout:等待最长时间
        :param interval:检测时间间隔
        :return:是否离开
        """
        try:
            # 如果规定时间内离开返回True, 否则报错
            return WebDriverWait(self, timeout, interval).until_not(presence_of_element_located((by, value)))
        except TimeoutException:
            return False

    def wait_presence_of_elements(self, by, value, timeout=10, interval=0.5) -> List[WebElement]:
        """
            等待多个元素出现
        :param by:查找依据
        :param value:查找元素
        :param timeout:等待最长时间
        :param interval:检测时间间隔
        :return:查找到的元素
        """
        return WebDriverWait(self, timeout, interval).until(presence_of_all_elements_located((by, value)))

    def wait_title_contains(self, content, timeout=2, interval=0.5):
        """
            等待判断标题是否包含指定字符
        :param content:是否包含的字符
        :param timeout:等待最长时间
        :param interval:检测时间间隔
        :return:bool类型,是否包含
        """
        try:
            return WebDriverWait(self, timeout, interval).until(title_contains(content))
        except TimeoutException:
            return False

    def wait_url_contains(self, content, timeout=2, interval=0.5):
        """
            等待地址栏是否包含指定字符
        :param content:是否包含的字符
        :param timeout:等待最长时间
        :param interval:检测时间间隔
        :return:bool类型,是否包含
        """
        try:
            return WebDriverWait(self, timeout, interval).until(url_contains(content))
        except TimeoutException:
            return False

    def move_to_element(self, by, value):
        """
            鼠标移动都某个元素
        :param by:查找依据
        :param value:值
        """
        action = ActionChains(self)
        action.move_to_element(self.wait_presence_of_element(by, value))
        action.perform()
