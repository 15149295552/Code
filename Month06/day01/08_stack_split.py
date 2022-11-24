'''
组合与拆分
'''
import numpy as np

a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)

#垂直方向
res = np.vstack((a,b))
print(res)
print(res.shape)

a,b = np.vsplit(res,2)
print(a)
print(b)

#水平方向
res = np.hstack((a,b))
print(res)
print(res.shape)

a,b = np.hsplit(res,2)
print(a)
print(b)

#深度方向
res = np.dstack((a,b))
print(res)
print(res.shape)

a,b = np.dsplit(res,2)
print(a)
print(b)




