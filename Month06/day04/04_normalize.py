'''
归一化:将每个数值转换为比率形式(0-1)
'''
import numpy as np

raw_sample = np.array([[10.0,20.0,5.0],
                       [8.0,10.0,1.0]])

nor_sample = raw_sample.copy()

for row in nor_sample:
    row /= abs(row).sum()

print(nor_sample)

#基于Sklearn提供的API实现归一化
import sklearn.preprocessing as sp

res = sp.normalize(raw_sample,norm='l1')
print(res)







