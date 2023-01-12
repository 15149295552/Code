"""
    写入Excel
"""
import pandas as pd
from pandas import ExcelWriter

df_data01 = pd.read_excel("01餐饮数据.xlsx")
new_data1 = df_data01[df_data01["城市"] == "北京"]
# 1. 覆盖写入到一个excel
# 语法:DataFrame对象.to_excel("文件名.xlsx",index=False)
new_data1.to_excel("北京餐厅.xlsx", index=False)

# 2. 多个表追加写入到一个excel
# 注意：该文件必须存在,否则报错
# 使用with语句,可以保证cpu离开缩进代码块时绝对关闭文件
# 语法：
# with ExcelWriter("文件名.xlsx", mode="a", if_sheet_exists="replace") as excel:
#     DataFrame对象.to_excel(excel,index=False, sheet_name="子表名称")
with ExcelWriter("北京和杭州.xlsx", mode="a", if_sheet_exists="replace") as excel:
    new_data2 = df_data01[df_data01["城市"] == "杭州"]
    new_data2.to_excel(excel, index=False, sheet_name="杭州")
    df_data01.to_excel(excel, index=False, sheet_name="北京")
