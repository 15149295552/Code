"""
    反反爬浏览器
"""
# 不使用"反反爬浏览器"每次都会进行"新手引导"
# with Chrome() as driver:
#     driver.get("https://www.douyin.com/")
#     input()

# 浏览器  <-登录-> 服务器
# ...
# 浏览器  -信息-> 服务器

# 查看方式：chrome://version/
# 个人资料路径：/home/tarena/.config/google-chrome
#            C:\Users\QTX\AppData\Local\Google\Chrome\User Data
# from selenium.webdriver import Chrome


import os
from selenium.webdriver import Chrome, ChromeOptions
import platform

options = ChromeOptions()
os_name = platform.system()
dir = ""
if 'Windows' == os_name:
    dir = r"C:\Users\%s\AppData\Local\Google\Chrome\User Data" % os.getlogin()
elif 'Linux' == os_name:
    dir = "/home/%s/.config/google-chrome" % os.getlogin()
options.add_argument("user-data-dir=" + dir)  # 设置用户数据目录
# 禁用启用Blink运行时的功能
options.add_argument("--disable-blink-features=AutomationControlled")
# 去除浏览器检测框
options.add_experimental_option("excludeSwitches", ["enable-automation"])
with Chrome(options=options) as driver:
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
                            Object.defineProperty(navigator, 'webdriver', {
                                get: () => undefined
                            })
    """})  # 再次覆盖window.navigator.webdriver的值
    driver.get("https://www.douyin.com/")
    input()
