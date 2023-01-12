"""
    定位器

"""
import pandas as pd

df_data = pd.read_excel("01餐饮数据.xlsx")
df_data2 = pd.read_excel("01餐饮数据.xlsx", index_col="店名")

# 位置索引
# 对象名.iloc[行选择器, 列选择器]
# 单选
print(df_data.iloc[0, 0])
# 切片
print(df_data.iloc[:3, -3:])
# 多选
print(df_data.iloc[[0, 5, 7, 10], [0, 3]])
# 不支持条件


# 标签索引
# 单选
print(df_data2.loc["小东北私房菜", "城市"])
# 切片
print(df_data2.loc["京门小院儿":"慈孝宫", "类型":"口味"])
# 多选
print(df_data2.loc[["京门小院儿", "慈孝宫"], ["类型", "口味"]])
# 条件
print(df_data.loc[df_data["城市"] == "北京", ["店名", "城市"]])

# 单选/切片/多选/条件
print(df_data.iloc[0,-3:])
print(df_data2.loc["京门小院儿":"慈孝宫", ["类型", "口味"]])
