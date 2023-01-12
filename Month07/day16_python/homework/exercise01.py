"""
    1. 在"02财务数据.xlsx"中完成下列操作
    --拆分表格
    将所属区域中"苏州"存入新excel中
    将所属区域中"无锡"存入新excel中
    将所属区域中"北京"存入新excel中
    --将以上3个表格合并为1个表格
"""
import pandas as pd

df_data = pd.read_excel("02财务数据.xlsx")
# 拆分
df_data[df_data["所属区域"] == "苏州"].to_excel("苏州.xlsx",index=False)
df_data[df_data["所属区域"] == "无锡"].to_excel("无锡.xlsx",index=False)
df_data[df_data["所属区域"] == "北京"].to_excel("北京.xlsx",index=False)

# 合并
df1 = pd.read_excel("苏州.xlsx")
df2 = pd.read_excel("无锡.xlsx")
df3 = pd.read_excel("北京.xlsx")
pd.concat([df1,df2,df3],ignore_index=True).to_excel("合并.xlsx",index=False)




