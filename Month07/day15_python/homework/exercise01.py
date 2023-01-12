"""
(1)读取02财务数据.xlsx
(2)定位列
# 标签索引
-- 单个：所属区域
-- 多个：产品类别+金额
# 位置索引
-- 切片：后3列
(3)定位行
-- 切片：前10行
        从第三行到第十五行
-- 条件：所有北京信息
        所有彩盒信息
(4)写入excel
将所有苏州的行数据存储在"苏州.xlsx"中
将订购日期列和金额列存储在"财务数据2.xlsx"中
将所有"彩盒"、"睡袋"、"宠物用品"数据存入"财务数据3.xlsx"文件的三个子表中
"""

import pandas as pd

df_data = pd.read_excel("02财务数据.xlsx")
# 列
print(df_data["所属区域"])
print(df_data[["产品类别", "金额"]])
print(df_data[df_data.columns[-3:]])

# 行
print(df_data[:10])
print(df_data[2:15])

print(df_data[df_data["所属区域"] == "北京"])
print(df_data[df_data["产品类别"] == "彩盒"])
print(df_data[(df_data["所属区域"] == "北京") & (df_data["产品类别"] == "彩盒")])
print(df_data[(df_data["所属区域"] == "北京") | (df_data["产品类别"] == "彩盒")])
