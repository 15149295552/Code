'''
测试时间日期类型
'''
import numpy as np

data = np.array(['2020','2021-01-01','2022-01-01 01:01:01',
                 '1970-01-01','1970-01-02'])
print(data)
print(data.dtype)

dates = data.astype('datetime64[s]') #[D]精确到天
print(dates)
print(dates.dtype)

#将时间日期类型,转为整型
val = dates.astype('int32')
print(val)