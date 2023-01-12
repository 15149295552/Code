"""
    爬取某人抖音账号中所有短视频信息
"""
import time

from pandas import DataFrame
from selenium.webdriver.common.by import By

from common.selenium_tools import SeleniumHelper

# 所有行：//li[@class="Eie04v01"]
#    链接：  ./a                          href属性
#    标题：  ./a/p                         文本
#    点赞数:     文本
with SeleniumHelper() as driver:
    # 访问某人的抖音账号
    driver.get(
        "https://www.douyin.com/user/MS4wLjABAAAA4L5xd8u9GS8LQVl-yK9x5j2h6mrK_G7Rw_jAW8k8QSmphUnPRsvu0pRgs1TIjokL?vid=7168443208668581123")
    list_video = []
    # time.sleep(5)
    for item in driver.find_elements(By.XPATH, '//li[@class="Eie04v01"]'):
        dict_info = {
            "标题": item.find_element(By.XPATH, './a/p').text,
            "点赞数": item.find_element(By.XPATH, './/span[@class="jjKJTf4P author-card-user-video-like"]').text,
            "链接": item.find_element(By.XPATH, './a').get_attribute("href"),
        }
        list_video.append(dict_info)
    DataFrame(list_video).to_excel("某抖音账号所有短视频信息.xlsx",index=False)