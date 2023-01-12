"""
    DataFrame 定位
"""
import pandas as pd

df_data01 = pd.read_excel("01餐饮数据.xlsx")
# 指定标签索引
df_data02 = pd.read_excel("01餐饮数据.xlsx",index_col="店名")



# 一、列
# -- DataFrame对象[列名]
print(df_data01["店名"])
print(df_data01[["店名", "点评"]])
# print(df_data01["人均":"服务"])
# 注意：标签索引不支持切片

# 因为columns支持位置索引、切片、多选,所以可以间接操作列
print(df_data01.columns)  # Index(['店名', '城市', '类型', '点评', '人均', '口味', '环境', '服务'], dtype='object')
print(df_data01[df_data01.columns[0]])  # 第一列
print(df_data01[df_data01.columns[:3]])  # 第三列
print(df_data01[df_data01.columns[[0, 3, 5, 6]]])  # 第三列

# 位置索引
# 标签索引
# -- 单个、切片、多个、条件
# 二、行
print(df_data01[:3])
print(df_data01[df_data01["类型"] == "私房菜"])

print(df_data02)

# print(df_data02["梧桐宇私房菜":"小东北私房菜"])
# print(df_data02["梧桐宇私房菜"])


# 注意：不支持位置索引与标签索引的单选/多选
# print(df_data01[0])
# print(df_data01[[1,5]])
