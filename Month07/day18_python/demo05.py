"""

"""
from selenium.webdriver.common.by import By

from common.selenium_tools import SeleniumHelper

with SeleniumHelper() as driver:
    driver.get("https://creator.douyin.com/creator-micro/data/stats/video")
    # time.sleep(2) # 强制等待2秒
    # driver.find_element(By.XPATH,'//div[@class="semi-select-selection"]').click()
    # time.sleep(2)
    # driver.find_element(By.XPATH,'//div[@class="semi-select-option-list semi-select-option-list-chosen"]/div[3]').click()

    # 显式等待5秒(5秒内找到会立即向下执行，5秒外会报错)
    driver.wait_presence_of_element(By.XPATH, '//div[@class="semi-select-selection"]').click()
    driver.wait_presence_of_element(By.XPATH,
                                    '//div[@class="semi-select-option-list semi-select-option-list-chosen"]/div[3]').click()
