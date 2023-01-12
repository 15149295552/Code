"""
练习:在"02财务数据.xlsx"中查询下列数据

前三行的后五列数据

所有北京的行数据

区域和金额列数据

金额大于50000的区域

数量大于100的产品类别和成本

"""
import pandas as pd

df_data = pd.read_excel("homework/02财务数据.xlsx")
print(df_data.index)
# 前三行的后五列数据
print(df_data.iloc[:3, -5:])
# 所有北京的行数据
# print(df_data.loc[df_data["所属区域"] == "北京"])
print(df_data[df_data["所属区域"] == "北京"])

# 所属区域和金额列数据
# print(df_data.loc[:,["所属区域","金额"]])
print(df_data[["所属区域","金额"]])

# 金额大于50000的所属区域
print(df_data.loc[df_data["金额"] > 5000, "所属区域"])

# 数量大于100的产品类别和成本
print(df_data.loc[df_data["数量"] > 100, ["产品类别","成本"]])
