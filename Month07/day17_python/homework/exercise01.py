"""
    1. 在"07摄影公司销售数据.xlsx"文件成下列操作
    -- 根据订单来源查看总价，统计最好的2个来源
    -- 根据拍摄套系查看总价，统计最好的3个产品
    -- 根据月份与角色1查看总价，统计最好的3个月份与最好的3个销售
"""
import pandas as pd
import numpy as np

df_data = pd.read_excel("07摄影公司销售数据.xlsx")
df_table = df_data.pivot_table(
    values="总价", index="订单来源", aggfunc=np.sum
)
df_table.sort_values("总价", ascending=False, inplace=True)
print("全年最好的2个订单来源：%s" % (df_table.index[:2].str.cat(sep=",")))

df_table = df_data.pivot_table(
    values="总价", index="拍摄套系", aggfunc=np.sum
)
df_table.sort_values("总价", ascending=False, inplace=True)
print("全年最好的3个产品：%s" % (df_table.index[:3].str.cat(sep=",")))

df_data["月份"] = df_data["创建时间"].dt.month
df_table = df_data.pivot_table(
    values="总价", index="月份", columns="角色1", aggfunc=np.sum,
    margins=True, margins_name="总计"
)
df_table.sort_values("总计", ascending=False, inplace=True, axis="index")
df_table.sort_values("总计", ascending=False, inplace=True, axis="columns")
df_table.drop("总计", axis="index", inplace=True)
df_table.drop("总计", axis="columns", inplace=True)
df_table.index = df_table.index.astype("str")
print("全年最好的3个月份：%s" % (df_table.index[:3].str.cat(sep=",")))
print("全年最好的3个销售：%s" % (df_table.columns[:3].str.cat(sep=",")))

