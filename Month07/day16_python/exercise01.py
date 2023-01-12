"""
    批量操作
"""
from pandas import ExcelWriter
import pandas as pd

# 函数名称可以随意,但是参数必须有一个,得到的数据就是单元格的旧数据
# 返回值就是单元格中的新数据
def get_cell_value(item:str):
    if type(item) != str:return item
    if item.endswith("w"):
        return float(item[:-1]) * 10000
    return float(item)

# 多个子表追加到一个excel文件中
with ExcelWriter("05摄影类爆款短视频.xlsx", mode="a", if_sheet_exists="replace") as file:
    # 读取所有子表,指定千位符
    for name,df in pd.read_excel(file, sheet_name=None,thousands=",").items():
        # print(df[df.columns[1:-1]].applymap(get_cell_value))
        df[df.columns[1:-1]] = df[df.columns[1:-1]].applymap(get_cell_value)
        df.to_excel(file, sheet_name=name, index=False)