"""
    读取Excel
"""
import pandas as pd

#
df_data01 = pd.read_excel("01餐饮数据.xlsx")

# 可以指定标签索引
df_data02 = pd.read_excel("01餐饮数据.xlsx",index_col="店名")

# 读取指定的子表
df_data03 = pd.read_excel("03字符串处理.xlsx",sheet_name="字符串处理练习")
# print(df_data03)

# 读取所有子表
# 注意：{子表名称:DataFrame对象,子表名称:DataFrame对象}
df_data04 = pd.read_excel("03字符串处理.xlsx",sheet_name=None)
print(df_data04)