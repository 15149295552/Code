'''
二值化:设定阈值，大于阈值--》1 小于等于阈值--》0
'''
import numpy as np

data = np.array([[61.1,98.9,12.3],
                 [77.6,88.8,66.6],
                 [22.2,33.3,55.6]])
bin_data = data.copy()

# bin_data[bin_data <= 60] = 0
# bin_data[bin_data > 60] = 1
bin_data = np.where(bin_data>60,1.0,0.0)

print(bin_data)

#基于sklearn提供的API实现二值化
import sklearn.preprocessing as sp

biner = sp.Binarizer(threshold=60)
res = biner.transform(data)
print(res)



