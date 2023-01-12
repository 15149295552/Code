"""
    练习：在"02财务数据.xlsx"中处理下列数据
        增加利润列
        数量小于10的改为10
        删除金额小于10000的行
"""
import pandas as pd

df_data = pd.read_excel("homework/02财务数据.xlsx")
df_data["利润"] = df_data["金额"] - df_data["成本"]

df_data.loc[df_data["数量"] < 10, "数量"] = 10

df_data.drop(df_data[df_data["金额"] < 10000].index, inplace=True)

df_data.to_excel("测试.xlsx", index=False)
