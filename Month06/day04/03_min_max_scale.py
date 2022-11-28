'''
范围缩放
缩小列与列之间的差异:将每列的最小值和最大值设为相同的区间
'''
import numpy as np

raw_sample = np.array([[1.0,2.0,3.0],
                       [4.0,5.0,9.0],
                       [7.0,8.0,11.0]])

mms_sample = raw_sample.copy()

# 1.用原始数据 - 最小值
# 2.用减完的结果  /  原始数据中最大值-最小值

for col in mms_sample.T:
    col_min = col.min()#每列的最小值
    col_max = col.max()#每列的最大值
    col -= col_min #减完之后的结果
    col /= (col_max - col_min)

print(mms_sample)

#基于Sklearn提供的API实现范围缩放
import sklearn.preprocessing as sp

mms = sp.MinMaxScaler(feature_range=(0,1)) #模型
# mms.fit(raw_sample) #训练出来转换的规则,最小值为0,最大值为1,中间数据进行同比例的缩放
# res = mms.transform(raw_sample)
res = mms.fit_transform(raw_sample)
print(res)



