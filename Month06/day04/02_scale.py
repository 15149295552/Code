'''
标准化:均值移除
缩小列与列之间的差异, 将每列的均值变为0,标准差变为1
'''
import numpy as np

raw_sample = np.array([[3.0,-100.0,2000.0],
                       [0.0,400.0,3000.0],
                       [1.0,-400.0,2000.0]])

std_sample = raw_sample.copy()

# 1.用原始数据 - 当前列的平均值，得到离差
# 2.离差 /  原始数据的标准差
for col in std_sample.T:
    col_mean = col.mean()#每列的平均值
    col_std = col.std()#每列的标准差
    col -= col_mean #col离差
    col /= col_std

print(std_sample)
print(std_sample.mean(axis=0))
print(std_sample.std(axis=0))

#基于sklearn提供的API实现均值移除
import sklearn.preprocessing as sp #数据预处理

res = sp.scale(raw_sample)
print('==' *30)
print(res)
print(res.mean(axis=0))
print(res.std(axis=0))





