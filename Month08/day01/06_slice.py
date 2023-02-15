'''多维数组的切片'''
import numpy as np

ary = np.arange(1,19).reshape(2,3,3)
print(ary)
#第0页的前两行的前两列
print(ary[:1,:2,:2])
#第一页的1,3行和1,3列
print(ary[1,::2,::2])
#所有页的后两行的后两列
print(ary[:,-2:,-2:])

ary = np.arange(1,22).reshape(7,3)

# 拿到所有行的，不要最后一列 (二维数据)  x
print(ary[:,:2])
# 拿到所有行的，只要最后一列(一维数据)  y
print(ary[:,-1])








