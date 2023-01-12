"""
    爬取祁大圣讲编程抖音账号中所有短视频信息(标题/链接/点赞数)
    https://www.douyin.com/user/MS4wLjABAAAABBOT3Hngfay81U0YyAJ1nbNmxNfSvZFms3BiMHR9wlI
"""
from pandas import DataFrame
from selenium.webdriver.common.by import By

from common.selenium_tools import SeleniumHelper

with SeleniumHelper() as driver:
    driver.get(
        "https://www.douyin.com/user/MS4wLjABAAAABBOT3Hngfay81U0YyAJ1nbNmxNfSvZFms3BiMHR9wlI")
    list_video = []
    for item in driver.find_elements(By.XPATH, '//li[@class="Eie04v01"]'):
        dict_info = {
            "标题": item.find_element(By.XPATH, './a/p').text,
            "点赞数": item.find_element(By.XPATH, './/span[@class="jjKJTf4P author-card-user-video-like"]').text,
            "链接": item.find_element(By.XPATH, './a').get_attribute("href"),
        }
        list_video.append(dict_info)
    DataFrame(list_video).to_excel("祁大圣讲编程抖音账号所有短视频信息.xlsx",index=False)