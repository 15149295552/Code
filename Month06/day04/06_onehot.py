'''
独热编码:
将特征中的特征值转换为由1个1和若干个0组成的形式
'''
import numpy as np
import sklearn.preprocessing as sp

raw_sample = np.array([[1,3,2],
                       [7,5,4],
                       [1,8,6],
                       [7,3,9]])

encoder = sp.OneHotEncoder(sparse=False, #不采用稀疏矩阵
                           dtype='int32')#元素类型

res = encoder.fit_transform(raw_sample)

print(res)

inv_res = encoder.inverse_transform(res)
print(inv_res)





