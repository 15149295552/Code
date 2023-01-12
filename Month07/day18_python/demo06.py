"""
    抖音创作者服务平台采集
    语法速查手册
        https://www.processon.com/view/link/6389c900e0b34d0711c0555f
"""
from selenium.webdriver.common.by import By
from common.selenium_tools import SeleniumHelper

with SeleniumHelper() as driver:
    url = "https://creator.douyin.com/creator-micro/data/stats/video"
    driver.get(url)
    if driver.wait_url_contains(url) == False:
        # 登录
        driver.wait_presence_of_element(By.XPATH,'//span[@class="login"]').click()
        driver.wait_presence_of_element(By.XPATH,'//span[@class="semi-button-content"]').click()
        # 等待用户扫码成功后窗口消失
        if driver.wait_leave_of_element(By.XPATH,'//div[@class="semi-modal-content"]'):
            print("登录成功")
            driver.get(url)
        else:
            print("登录失败")
            exit()
    # 显式等待5秒(5秒内找到会立即向下执行，5秒外会报错)
    driver.wait_presence_of_element(By.XPATH, '//div[@class="semi-select-selection"]').click()
    driver.wait_presence_of_element(By.XPATH,'//div[@class="semi-select-option-list semi-select-option-list-chosen"]/div[3]').click()
    input()