"""
    黄金交叉
"""
import pandas as pd
import numpy as np

df_data = pd.read_excel("07摄影公司销售数据.xlsx")

df_data["月份"] = df_data["创建时间"].dt.month
df_table = df_data.pivot_table(
    values="总价", index="月份", columns="拍摄套系",
    aggfunc=np.sum, margins=True, margins_name="总计"
)
df_table.sort_values("总计", ascending=False, inplace=True, axis="index")
df_table.sort_values("总计", ascending=False, inplace=True, axis="columns")
df_table.drop("总计", axis="index", inplace=True)
df_table.drop("总计", axis="columns", inplace=True)

print(df_table["套餐三"])

print(df_table["老板定制"])

for r in range(len(df_table["套餐三"]) - 1):
    # 当前点：套餐三 > 老板定制
    # 下一点：套餐三 < 老板定制
    if df_table.iloc[r]["套餐三"] > df_table.iloc[r]["老板定制"] and df_table.iloc[r + 1]["套餐三"] < df_table.iloc[r + 1][
        "老板定制"]:
        print("黄金交叉")

# list_cross = []
# for c1 in range(len(df_table.columns) - 1):
# 	for c2 in range(c1 + 1, len(df_table.columns)):
# 		for r in range(len(df_table) - 1):
# 			if df_table.iloc[r, c1] > df_table.iloc[r, c2] and df_table.iloc[r + 1, c1] < df_table.iloc[r + 1, c2]:
# 				list_cross.append((df_table.index[r + 1], df_table.columns[c2]))
# print("发生黄金交叉的产品是：%s" % list_cross)
