"""
    练习1：在"02财务数据.xlsx"中完成下列操作

1.清洗数据

--删除所有空白行

--用0填充空白单元格

--删除重复行

2.数据透视表

将"所属区域"列和"产品类别"列进行分组，聚合"金额"列(求和)
行列根据"总计"降序排列
统计：
1.公司销售?个区域，根据业绩降序排列分别为?
2.公司销售?个产品，根据销售额降序排列分别为?
"""
import pandas as pd
import numpy as np

df_data = pd.read_excel("02财务数据.xlsx")
# 1.清洗数据
# --删除所有空白行
df_data.dropna(inplace=True, how="all")
# --用0填充空白单元格
df_data.fillna(0, inplace=True)
# --删除重复行
df_data.drop_duplicates(inplace=True)

# 2.
df_table = df_data.pivot_table(
    index="所属区域", values="金额",
    aggfunc=np.sum, columns="产品类别",
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
print("公司%s个运营区域,根据业绩降序分别为%s" % (len(df_table), df_table.index.str.cat(sep=",")))
print("公司销售%s个产品,根据业绩降序分别为%s" % (len(df_table.columns), df_table.columns.str.cat(sep=",")))
