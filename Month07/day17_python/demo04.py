"""
    采集百度电影热搜-无界面浏览器

"""
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from pandas import DataFrame

# with Chrome() as driver:
option = ChromeOptions()
option.add_argument("--headless")
with Chrome(options=option) as driver:
    driver.get("https://top.baidu.com/board?tab=movie")
    list_result = []
    # 所有行
    for item in driver.find_elements(By.XPATH, '//div[@class="category-wrap_iQLoo "]'):
        # 改行的列xpath必须使用相对路径.开头
        dict_movie = {
            "电影名称": item.find_element(By.XPATH, './/div[@class="c-single-text-ellipsis"]').text,
            "电影类型": item.find_element(By.XPATH, './/div[@class="content_1YWBm"]/div[1]').text,
            "演员": item.find_element(By.XPATH, './/div[@class="content_1YWBm"]/div[2]').text,
            "剧情": item.find_element(By.XPATH, './/div[@class="c-single-text-ellipsis desc_3CTjT"]').text,
            "指数": item.find_element(By.XPATH, './/div[@class="hot-index_1Bl1a"]').text,
        }
        list_result.append(dict_movie)
    DataFrame(list_result).to_excel("百度热搜电影信息.xlsx", index=False)
