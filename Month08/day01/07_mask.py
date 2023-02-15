'''
数组的掩码操作(布尔掩码,索引掩码)
'''

import numpy as np

ary = np.arange(1,101)
mask = ary % 3 == 0
print(ary[mask])
#能同时被3和7整除的数字

print('=' * 30)

# mask = (ary % 3 == 0) & (ary % 7 == 0)
# mask = ary % 21 == 0
res1 = ary[ary % 3 == 0]
res2 = res1[res1 % 7 == 0]
print(res2)

print('=' * 30)
#索引掩码
ary = np.array(['BMW','BENZ','AUDI','BYD'])
# mask = [3,0,2,1]
mask = [3,3,3,3,3,0,2,0,2,0,0,1,1,1]
print(ary[mask])
