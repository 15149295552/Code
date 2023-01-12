"""
    pandas 处理excel文件的神器
        入门
"""
import pandas as pd
from pandas import Series, DataFrame

df_data = pd.read_excel("01餐饮数据.xlsx")  # type:DataFrame
column01 = df_data["店名"]  # type:Series
row01 = df_data.iloc[0]  # type:Series
print(column01)
print(row01)
