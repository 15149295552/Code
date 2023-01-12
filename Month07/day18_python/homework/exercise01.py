"""
1.采集豆瓣电影排行榜(标题、信息、分数、点评人数)
https://movie.douban.com/chart

2.对豆瓣电影排行榜数据进行清洗后存储到Excel文件中
    "电影名称"列保留第一个
	增加"上映时间"列，保留第一个时间
	增加"主演"列，只保留演员姓名
	"评价人数"列，只保留数字
"""

from pandas import DataFrame
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

with Chrome() as driver:
    driver.get("https://movie.douban.com/chart")
    list_datas = []
    for item in driver.find_elements(By.XPATH, '//div[@class="pl2"]'):
        dict_data = {}
        dict_data["电影名称"] = item.find_element(By.XPATH, './a').text
        dict_data["电影描述"] = item.find_element(By.XPATH, './p[@class="pl"]').text
        dict_data["电影评分"] = item.find_element(By.XPATH, './/span[@class="rating_nums"]').text
        dict_data["评价人数"] = item.find_element(By.XPATH, './/span[@class="pl"]').text
        list_datas.append(dict_data)
    df_data = DataFrame(list_datas)
    df_data.to_excel("测试.xlsx", index=False)
    df_data["电影名称"] = df_data["电影名称"].str.split("/", expand=True)[0]
    df_data["上映时间"] = df_data["电影描述"].str.extract("(.*?)\(")
    df_data["主演"] = df_data["电影描述"].str.replace(".*?\(.*?\) /", "", regex=True)
    df_data["评价人数"] = df_data["评价人数"].str.extract("(\d+)")
    df_data.drop("电影描述", axis=1, inplace=True)
    df_data.to_excel("豆瓣电影排行榜.xlsx", index=False)
