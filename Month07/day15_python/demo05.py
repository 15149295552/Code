"""
    定制化数据处理
        excel 合并与拆分
"""
import pandas as pd

df_data = pd.read_excel("01餐饮数据.xlsx")

# 一拆多
df_data[df_data["城市"] == "北京"].to_excel("北京餐厅.xlsx",index=False)
df_data[df_data["城市"] == "大连"].to_excel("大连餐厅.xlsx",index=False)

# 多合一
df1 = pd.read_excel("北京餐厅.xlsx")
df2 = pd.read_excel("大连餐厅.xlsx")
pd.concat([df1,df2]).to_excel("合并.xlsx",index=False)