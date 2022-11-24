'''
DataFrame示例
'''
import numpy as np
import pandas as pd

data = [100,90,80,70,60]
df = pd.DataFrame(data,
                  index=['zs','ls','ww','sl','zq'],
                  columns=['score'])
# print(df)
# print(df.shape)

#通过二维列表构建DF
data = [['Alex',18],
        ['Tom',19],
        ['Jerry',20]]
df = pd.DataFrame(data,
                  index=['s01','s02','s03'],
                  columns=['Name','Age'])
# print(df)

#通过字典构建DataFrame
data = {'Name':['Tom','Jerry','Jack','Rose'],
        'Age':[18,18,20,20]}

df = pd.DataFrame(data)
# print(df)


data = {'one':pd.Series([1,2,3,4],
                        index=['a','b','c','d']),
        'two':pd.Series([1,2,4],
                        index=['a','b','d'])}
df = pd.DataFrame(data)
print(df)

print(df.axes)
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.empty)
print(df.ndim) #2
print(df.shape) #(4,2)
print(df.size) #8
print(df.values)
print(df.head(2))
print(df.tail(2))





