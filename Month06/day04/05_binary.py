'''
二值化
设定阈值,大于阈值-->1  小于等于阈值的-->0
'''
import numpy as np

raw_sample = np.array([[89.6,55.5,99.6],
                       [12.8,66.6,88.8],
                       [23.1,11.2,77.7]])
bin_sample = raw_sample.copy()

# 阈值:60
# 大于60-->1, 小于等于60-->0
# bin_sample[bin_sample <= 60] = 0
# bin_sample[bin_sample > 60] = 1
# print(bin_sample)
print(np.where(bin_sample>60,1.0,0.0))

#基于sklearn提供的API实现二值化
import sklearn.preprocessing as sp
biner = sp.Binarizer(threshold=60)

res = biner.transform(raw_sample)
print(res)



