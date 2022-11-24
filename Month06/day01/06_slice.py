'''
数组的切片
'''
import numpy as np

ary = np.arange(1,10).reshape(3,3)
print(ary)
#前两行的前两列
print(ary[:2,:2])
print(ary[::2,::2])
print(ary[:2,0])
print(ary[:2])

