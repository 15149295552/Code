'''
归一化：将每个元素转为相对比例（0-1）
'''
import numpy as np

data = np.array([[10.0,20.0,5.0],
                 [8.0,10.0,1.0]])
nor_data = data.copy()

for row in nor_data:
    row /= abs(row).sum()

print(nor_data)
print(nor_data.sum(axis=1))

# 基于sklearn提供的API实现归一化
import sklearn.preprocessing as sp

res = sp.normalize(data,norm='l1')
print(res)
print(res.sum(axis=1))
