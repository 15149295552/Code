"""
    使用自定义浏览器助手类
"""
from common.selenium_tools import SeleniumHelper

# 打开抖音后登录，再次打开就是登录状态
with SeleniumHelper() as driver:
    driver.get("https://www.douyin.com/")
    input()