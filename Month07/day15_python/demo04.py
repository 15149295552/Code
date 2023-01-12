"""
    定制化数据处理
        行
"""
import pandas as pd
from pandas import DataFrame

df_data = pd.read_excel("01餐饮数据.xlsx")
df_data02 = pd.read_excel("01餐饮数据.xlsx", index_col="店名")

# 1. 修改
df_data.iloc[0, 1] = "上海"
df_data.iloc[1, -3:] = [8, 9, 10]
df_data.loc[df_data["类型"] == "私房菜", ["口味", "城市"]] = [11, "首都"]

# 2.创建
# DataFrame([字典1,字典2])
df1 = DataFrame([{"店名": "全聚德", "人均": 230}, {"店名": "眉州东坡", "口味": 10}])

# DataFrame({"列名":[元素1,元素2],"列名":[元素1,元素2]})
df2 = DataFrame({"城市": ["北京", "上海"], "人均": [96, 99]})

# 3.添加
df_data = pd.concat([df1, df_data, df2], ignore_index=True)

# 4. 删除
# df_data.drop([0,5],inplace=True)
# df_data02.drop(["原点老板娘私房菜","小东北私房菜"],inplace=True)
# df_data.drop(df_data[df_data["城市"] == "北京"].index, inplace=True)

df_data.to_excel("测试.xlsx")
# df_data02.to_excel("测试.xlsx")
