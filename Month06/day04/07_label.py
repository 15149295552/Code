'''
标签编码器
根据字符串在特征中的位置(Ascii),为其提供一个数值,进行转换
'''
import numpy as np
import sklearn.preprocessing as sp

data = np.array(['benz','bmw','BYD','audi','bmw','audi','benz'])
# [2 3 0 1 3 1 2]
encoder = sp.LabelEncoder()

res = encoder.fit_transform(data)
print(res)

inv_res = encoder.inverse_transform(res)
print(inv_res)