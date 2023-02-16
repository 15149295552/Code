'''
独热编码:将每列的特征转为由1个1和若干个0组成的序列
'''
import numpy as np
import sklearn.preprocessing as sp

data = np.array([[1,3,2],
                 [7,5,4],
                 [1,8,6],
                 [7,3,9]])

encoder = sp.OneHotEncoder(sparse=False,#不采用稀疏格式
                           dtype='int32',
                           categories='auto')#自动编码

res = encoder.fit_transform(data)
print(res)

#解码
inv_res = encoder.inverse_transform(res)
print(inv_res)

