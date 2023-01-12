"""
    2. 在"08抖音后台短视频数据.xlsx"文件中清洗数据
    -- 将-改为0
    -- 将w改为*10000
"""
import pandas as pd

def get_cell_value(item: str):
    if item == "-": return 0
    if item.endswith("w"):
        return float(item[:-1]) * 10000
    return float(item)

df_data = pd.read_excel("08抖音后台短视频数据.xlsx")
df_data[df_data.columns[1:]] = df_data[df_data.columns[1:]].applymap(get_cell_value)
df_data.to_excel("08抖音后台短视频数据2.xlsx", index=False)
