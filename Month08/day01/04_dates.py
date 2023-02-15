'''时间日期类型
年月日之间使用“-”  时分秒使用“：”  1-9要使用01-09
'''
import numpy as np

data = ['2020','2021-01-01','2022-01-01 01:01:01',
        '1970-01-01','1970-01-02']
ary = np.array(data)
print(ary)
print(ary.dtype)
#将字符串类型，转换为时间日期类型 Y M D h m s
dates = ary.astype('datetime64[s]')
print(dates)
print(dates.dtype)

#将日期类型，转为int
res = dates.astype('int32')
print(res)
