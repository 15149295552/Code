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


def data_collection() -> list:
    """
        数据采集
    """
    with Chrome() as driver:
        driver.get("https://movie.douban.com/chart")
        list_data = []
        for item in driver.find_elements(By.XPATH, '//div[@class="pl2"]'):
            dict_data = {}
            dict_data["电影名称"] = item.find_element(By.XPATH, './a').text
            dict_data["电影描述"] = item.find_element(By.XPATH, './p[@class="pl"]').text
            dict_data["电影评分"] = item.find_element(By.XPATH, './/span[@class="rating_nums"]').text
            dict_data["评价人数"] = item.find_element(By.XPATH, './/span[@class="pl"]').text
            list_data.append(dict_data)
    return list_data


def data_cleaning(list_data: list) -> DataFrame:
    """
        数据清洗
    :param list_data:list类型的旧数据
    :return:DataFrame类型的新数据
    """
    df_data = DataFrame(list_data)
    df_data["电影名称"] = df_data["电影名称"].str.split("/", expand=True)[0]
    df_data["上映时间"] = df_data["电影描述"].str.extract("(.*?)\(")
    df_data["主演"] = df_data["电影描述"].str.replace(".*?\(.*?\) /", "", regex=True)
    df_data["评价人数"] = df_data["评价人数"].str.extract("(\d+)")
    df_data.drop("电影描述", axis=1, inplace=True)
    return df_data


def data_storage(df_data: DataFrame) -> None:
    """
        数据存储
    :param df_data:DataFrame类型的数据
    """
    df_data.to_excel("豆瓣电影排行榜.xlsx", index=False)


def main():
    """
        主逻辑
    """
    list_data = data_collection()
    df_data = data_cleaning(list_data)
    data_storage(df_data)


main()
