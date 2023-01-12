"""
    标准化数据清洗
"""
import pandas as pd

df_data = pd.read_excel("01餐饮数据.xlsx")
# 一、查看数据
# 空行、列信息
df_data.info()

# 重复行
# print(df_data[df_data.duplicated()]) # 行数据
print(df_data.duplicated().sum())  # 行数

# 二、删除空值
# df_data.dropna() # 返回新数据,原始数据不变
# df_data.dropna(inplace=True) # 改变原始数据
# df_data.dropna(inplace=True,axis=1) # 删除空列
df_data.dropna(inplace=True, how="all")  # 本行都为空时,才删除

# 三、填充空值
df_data.fillna(0, inplace=True)

# 四、删除重复
# df_data.drop_duplicates(inplace=True) # 全部列
# 指定重复列
# df_data.drop_duplicates(inplace=True,subset="店名")
# 保留后面的重复数据
df_data.drop_duplicates(inplace=True, subset="店名", keep="last")

df_data.to_excel("测试.xlsx", index=False)
