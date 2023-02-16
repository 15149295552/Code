'''
对小汽车数据的每列进行标签编码
'''
import numpy as np
import pandas as pd
import sklearn.preprocessing as sp

data = pd.read_csv('../data_test/car.txt',
                   header=None)

print(data.dtypes)

res_data = pd.DataFrame()
encoders = {}
for i in data:
    encoder = sp.LabelEncoder()
    res = encoder.fit_transform(data[i])
    res_data[i] = res
    encoders[i] = encoder
print(res_data)
print(encoders)

#解码
ret = pd.DataFrame()
for i in res_data:
    encoder = encoders[i]
    res = encoder.inverse_transform(res_data[i])
    ret[i] = res
print(ret)



