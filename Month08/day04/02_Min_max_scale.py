'''
范围缩放
缩小特征与特征之间的差异
将每一列的最小值和最大值设为相同的区间（0-1）
'''
import numpy as np

data = np.array([[3.0,-100.0,2000.0],
                 [0.0,400.0,3000.0],
                 [1.0,-400.0,2000.0]])
mms_data = data.copy()

#1.每列数据的元素-当前列的最小值
#2.用减完之后的结果  / 原始数据的最大值-最小值
for col in mms_data.T:
    col_min = col.min()
    col_max = col.max()
    col -= col_min
    col /= (col_max - col_min)

print(mms_data)

# 基于sklearn提供的API实现范围缩放
import sklearn.preprocessing as sp

#构建范围缩放器模型
mms = sp.MinMaxScaler()
# mms.fit(data)
# res = mms.transform(data)
res = mms.fit_transform(data)
print(res)


