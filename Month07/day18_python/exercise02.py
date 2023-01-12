"""
    抓取短视频评论信息
        https://www.douyin.com/video/7086723783322569998
"""
import time

from pandas import Series
from selenium.webdriver.common.by import By

from common.selenium_tools import SeleniumHelper

with SeleniumHelper() as driver:
    driver.get("https://www.douyin.com/video/7086723783322569998")
    while True:
        try:
            # 查找"暂时没有更多评论"的标签
            driver.find_element(By.XPATH, '//div[@class="BbQpYS5o HO1_ywVX"]')
            break
        except:
            driver.scroll_by(0, 1000)
            time.sleep(3)

    list_remark = list(map(lambda item: item.text, driver.find_elements(By.XPATH, '//span[@class="VD5Aa1A1"]')))
    Series(list_remark, name="评论").to_excel("Unity3D短视频评论.xlsx", index=False)
    input()
