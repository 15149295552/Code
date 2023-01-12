"""
    # 练习：在"07摄影公司销售数据.xlsx"中完成下列操作
    # 根据月份查看总价，统计全年业绩最好的三个月
"""
import pandas as pd

df_data = pd.read_excel("07摄影公司销售数据.xlsx")
df_data["月份"] = df_data["创建时间"].dt.month
# 相同项 -> 分组 -> 聚合 -> 排序 -> 结论
df_table = df_data.pivot_table(
    "总价", "月份", aggfunc="sum"
)
df_table.sort_values("总价", inplace=True, ascending=False)
df_table.index = df_table.index.astype("str")
print("全年业绩最好的三个月:%s" % (df_table.index[:3].str.cat(sep=",")))
