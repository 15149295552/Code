'''
数组的维度处理
'''
import numpy as np

#视图变维
ary = np.arange(1,19)
print(ary,ary.shape)

bry = ary.reshape(2,9)
print(bry)

ary[0] = 666
print(bry)

cry = bry.ravel()
print(cry)

#复制变维
print('==' * 20)
ary = np.arange(1,19).reshape(2,9)
bry = ary.flatten()

ary[0][0] = 999
print(ary)
print(bry)

#就地变维
print('==' * 20)

ary = np.arange(1,19)
ary.resize(1,1,1,2,3,3)

print(ary)


