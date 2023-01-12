"""
    数据统计
"""
import pandas as pd
import numpy as np

df_data = pd.read_excel("06销售数据.xlsx")

df_table = df_data.pivot_table(
    index="产品", values="总价",
    aggfunc=np.sum, columns="部门",
    margins=True, margins_name="总计"
)
# 行降序
df_table.sort_values("总计", inplace=True, ascending=False, axis="index")
# 列降序
df_table.sort_values("总计", inplace=True, ascending=False, axis="columns")
# 删除总计行
df_table.drop("总计", axis="index", inplace=True)
# 删除总计列
df_table.drop("总计", axis="columns", inplace=True)
# 结论：
print("公司销售%s个产品,根据业绩降序分别为%s"%(len(df_table),df_table.index.str.cat(sep=",")))
print("公司销售%s个部门,根据业绩降序分别为%s"%(len(df_table.columns),df_table.columns.str.cat(sep=",")))
