"""
    练习2：使用2个Series对象表达2列数据，并打印以下数据：
    -- 位置索引定位单个元素：陕西,广西,2
    -- 位置索引定位多个元素：台湾,浙江,香港
    -- 位置切片定位多个元素：182,2,6
"""
from pandas import Series

ser_region = Series(["台湾", "陕西", "浙江", "广西", "香港"], name="地区")
ser_new = Series([16, 182, 2, 6, 9], name="新增")
print(ser_region[1])
print(ser_region[3])
print(ser_new[2]) 
print(ser_region[[0, 2, 4]])
print(ser_new[1:4])
print(ser_new[ser_new > 10])
