"""
    练习：采集百度热搜小说榜
        https://top.baidu.com/board?tab=novel&sa=fyb_novel_31065
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pandas import Series

with Chrome() as driver:
    driver.get("https://top.baidu.com/board?tab=novel&sa=fyb_novel_31065")
    # list_result = []
    # for item in driver.find_elements(By.XPATH, '//div[@class="c-single-text-ellipsis"]'):
    #     list_result.append(item.text)
    list_result = list(map(lambda item: item.text, driver.find_elements(By.XPATH, '//div[@class="c-single-text-ellipsis"]')))
    series_title = Series(list_result, name="小说标题")
    series_title.to_excel("百度热搜小说标题.xlsx", index=False)
