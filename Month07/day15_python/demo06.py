"""
    字符串处理
"""
import pandas as pd
from pandas.core.strings import StringMethods

#
# my_str = StringMethods() # type:StringMethods
# my_str.replace(".*?\(.*?/","",regex=True)

df_data = pd.read_excel("03字符串处理.xlsx")

# 悲情三角 / 无限悲情 / 疯狂富作用(台) -> [悲情三角 ,  无限悲情 ,  疯狂富作用(台)]
# print(df_data["电影名称"].str.split("/"))
# [悲情三角 ,  无限悲情 ,  疯狂富作用(台)] -> DataFrame对象
# print(df_data["电影名称"].str.split("/",expand=True)[0])
df_data["电影名称"] = df_data["电影名称"].str.split("/", expand=True)[0]

# print(df_data["电影描述"].str.extract("(.*?)\("))
# print(df_data["电影描述"].str.extract("(.*?)/"))
df_data["上映时间"] = df_data["电影描述"].str.extract("(.*?)\(")

df_data["演员"] = df_data["电影描述"].str.replace(".*?\(.*?/", "", regex=True)

df_data["评价人数"] = df_data["评价人数"].str.extract("(\d+)")
df_data.to_excel("测试.xlsx", index=False)
