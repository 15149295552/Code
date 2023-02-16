'''
数据预处理：均值移除（标准化）
缩小特征与特征之间的差异
将每列的平均值变为0，标准差变为1
'''

import numpy as np

data = np.array([[3.0,-100.0,2000.0],
                 [0.0,400.0,3000.0],
                 [1.0,-400.0,2000.0]])

std_data = data.copy()

# 1.用当前列中的每个元素  -  当前列的平均值  得到离差
# 2.用离差  /  原始数据中当前列的标准差
for col in std_data.T:
    col_mean = col.mean()
    col_std = col.std()
    col -= col_mean
    col /= col_std
print(std_data)
print(std_data.mean(axis=0))
print(std_data.std(axis=0))

#基于sklearn提供的API实现均值移除
import sklearn.preprocessing as sp
print('='* 30)
res = sp.scale(data)
print(res)
print(res.mean(axis=0))
print(res.std(axis=0))


