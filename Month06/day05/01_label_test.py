'''
标签编码的练习
将数据中的元素转为数值类型
'''
import pandas as pd
import sklearn.preprocessing as sp

# 加载数据,car.txt  将数据转为标签编码的格式
data = pd.read_csv('../data_test/car.txt',
                   header=None)

# print(data.head())
# print(data.dtypes)
# 每列之间的离散值不同,为每列构建自己的标签编码器
#遍历dataframe,拿到的是每列的列名
# for i in data:
#遍历dataframe.items()  k拿到列名,v列的值

res_data = pd.DataFrame()
for k,v in data.items():
    encoder = sp.LabelEncoder()
    res = encoder.fit_transform(v)
    res_data[k] = res
print(res_data)

