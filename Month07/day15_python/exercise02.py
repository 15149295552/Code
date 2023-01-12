"""
    练习：在"02财务数据.xlsx"中清洗下列数据

    删除所有空白的行

    用0填充空白单元格

    删除重复行
"""
import pandas as pd

df_data = pd.read_excel("homework/02财务数据.xlsx")
df_data.dropna(inplace=True,how="all")
df_data.fillna(0,inplace=True)
df_data.drop_duplicates(inplace=True)
df_data.to_excel("测试.xlsx",index=False)