'''
数组的组合与拆分
'''
import numpy as np

x = np.arange(1,7).reshape(2,3)
y = np.arange(7,13).reshape(2,3)

#垂直方向
res = np.vstack((x,y))
print(res)

x,y = np.vsplit(res,2)
print(x)
print(y)

#水平方向
res = np.hstack((x,y))
print(res)

x,y = np.hsplit(res,2)
print(x)
print(y)

#深度方向
res = np.dstack((x,y))
print(res)

x,y = np.dsplit(res,2)
print(x)
print(y)


