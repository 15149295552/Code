"""
    练习1：采集百度热搜游戏榜(名称、类型、指数)
"""
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from pandas import DataFrame

with Chrome() as driver:
    driver.get("https://top.baidu.com/board?tab=game")
    list_result = []
    # 所有行
    for item in driver.find_elements(By.XPATH, '//div[@class="category-wrap_iQLoo square_1ULM9"]'):
        # 改行的列xpath必须使用相对路径.开头
        dict_game = {
            "游戏名称": item.find_element(By.XPATH, './/div[@class="c-single-text-ellipsis"]').text,
            "游戏类型": item.find_element(By.XPATH, './/div[@class="intro_1l0wp"]').text,
            "指数": item.find_element(By.XPATH, './/div[@class="hot-index_1Bl1a"]').text,
        }
        list_result.append(dict_game)
    DataFrame(list_result).to_excel("百度热搜游戏榜.xlsx", index=False)
