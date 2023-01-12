"""
    时间处理
"""
import pandas as pd
import numpy as np

df_data = pd.read_excel("07摄影公司销售数据.xlsx")

# df_data["月份"] = df_data["创建时间"].dt.month
# weekday不是实例方法，不要加小括号
df_data["星期"] = df_data["创建时间"].dt.weekday + 1
df_table = df_data.pivot_table(
    values="总价",
    index="星期",
    aggfunc=np.sum
)
df_table.sort_values("总价",ascending=False,inplace=True)
# 将标签索引改为字符串类型
df_table.index = df_table.index.astype("string")
print("每周业绩最好的三天是%s"%(df_table.index[:3].str.cat(sep=",")))

