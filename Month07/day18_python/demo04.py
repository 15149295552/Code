"""
    爬取某人抖音账号中所有短视频信息
"""
import time

from pandas import DataFrame
from selenium.webdriver.common.by import By

from common.selenium_tools import SeleniumHelper

with SeleniumHelper() as driver:
    driver.get(
        "https://www.douyin.com/user/MS4wLjABAAAAb4b5X-nNL8bEJv1WtUAfxVPdLOFNZftqHYPk5_FZqJXj2AhqfcyvX0mvbTUkNHZd?vid=7173332388968205581")
    while True:
        try:
            # 如果标签存在返回,否则报错
            driver.find_element(By.XPATH,'//div[@class="Bllv0dx6"]') # "没有更多视频"
            break # 执行到本行说明没有报错,也就是没有更多视频了
        except:
            # 如果程序报错,进入当前代码块 -> 说明还有短视频,需要向下滚动
            driver.scroll_by(0, 1000)
            time.sleep(3)
    list_video = []
    for item in driver.find_elements(By.XPATH, '//li[@class="Eie04v01"]'):
        dict_info = {
            "标题": item.find_element(By.XPATH, './a/p').text,
            "点赞数": item.find_element(By.XPATH, './/span[@class="jjKJTf4P author-card-user-video-like"]').text,
            "链接": item.find_element(By.XPATH, './a').get_attribute("href"),
        }
        list_video.append(dict_info)
    DataFrame(list_video).to_excel("达内账号所有短视频信息.xlsx",index=False)