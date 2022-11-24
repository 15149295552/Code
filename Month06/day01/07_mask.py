'''
数组的掩码操作
布尔掩码,索引掩码
'''
import numpy as np

#布尔掩码
ary = np.arange(1,10)
mask = [True,False,True,False,True,False,True,False,True]
res = ary[mask]
print(res)

#输出1-100以内3的倍数
ary = np.arange(1,101)
mask = ary % 3 == 0
print(ary[mask])

#输出100以内同时被3和7整除的数字
# res = ary[ary%3==0]
# print(res[res%7==0])
mask = (ary % 3 == 0) & (ary % 7 == 0)
print(ary[mask])

#索引掩码
ary = np.array(['bmw','audi','benz','BYD'])
# mask = [3,0,1,2]
# print(ary[mask])
mask = [3,3,3,0,1,0,1,0,3,3,0,2,2,1]
print(ary[mask])


