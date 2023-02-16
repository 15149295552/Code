'''
标签编码
将字符串转为数值
'''
import numpy as np
import sklearn.preprocessing as sp

#一维
data = np.array(['bmw','benz','audi','bmw','audi',
                 'BYD','Tesla'])
#[0 1 2 0 2 3 4]

#[4 3 2 4 2 0 1]
encoder = sp.LabelEncoder()

res = encoder.fit_transform(data)
print(res)

print(encoder.inverse_transform(res))


#二维
data_2d = np.array([['bmw','m3','black'],
                    ['bmw','m4','green'],
                    ['audi','RS6','gray'],
                    ['benz','AmgGT50','white']])

ret = []
for col in data_2d.T:
    #因为每列的特征值不同，为每列构建自己的编码器
    encoder = sp.LabelEncoder()
    res = encoder.fit_transform(col)
    ret.append(res)

ret = np.array(ret).T
print(ret)