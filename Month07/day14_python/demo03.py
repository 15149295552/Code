"""
    Series
"""
from pandas import Series

# 一、表达列
# 1. 创建
# 对象名 = Series(列表, name="列名")
column_server = Series([6.9, 7.1, 7.9], name="服务")
# 2. 定位
# -- 位置索引: 对象名[整数]
print(column_server[0])
# -- 位置索引切片: 对象名[整数:整数:整数]
print(column_server[:2])
# -- 位置索引多选: 对象名[[整数,整数]]
print(column_server[[0, 2]])
# -- 位置索引多选: 对象名[条件]
print(column_server[column_server > 7])

# 3. 运算
print(column_server > 7) # 使用每个元素分别与数字比较
print(column_server + 1) # 使用每个元素分别与数字相加
column_server += 1
print(column_server)

# 二、表达行
# 1. 创建
row_xdb = Series({"店名":"小东北私房菜","城市":"北京","点评":1})
# 2. 定位
# -- 标签索引:对象名[标签]
print(row_xdb["店名"])
# -- 标签索引:对象名[标签:标签:整数]
# 注意：包含结束值
print(row_xdb["店名":"点评"])
# -- 标签索引:对象名[[标签,标签]]
print(row_xdb[["店名","点评"]])
