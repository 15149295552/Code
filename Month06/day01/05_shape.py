'''
数组的维度处理
'''
import numpy as np

ary = np.arange(1,19)
print(ary)
print(ary.shape)
#视图变维
bry = ary.reshape(2,9)
print(bry)
print(bry.shape)

ary[0] = 666
print(bry)

bry = bry.ravel()
print(bry)

#复制变维
print('=' * 30)
ary = np.arange(1,9).reshape(2,2,2)
print(ary)

bry = ary.flatten()
print(bry)
ary[0,0,0] = 666
print(bry)

#就地变维
ary = np.arange(1,9)
ary.resize(2,2,2)
print(ary)



