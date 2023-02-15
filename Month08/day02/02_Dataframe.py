'''
dataframe示例
'''
import numpy as np
import pandas as pd

df = pd.DataFrame([1,2,3,4,5])
# print(df)
# print(df.shape)

df = pd.DataFrame([['Tom',18],
                   ['Jerry',18],
                   ['Alex',20]],
                  index=['s01','s02','s03'],
                  columns=['name','age'])
# print(df)

df = pd.DataFrame({'Name':['Tom','Jerry','Jack','Rose'],
                   'Age':[18,18,20,20]})
# print(df)

df = pd.DataFrame({'Name':pd.Series(['Tom','Jerry','Jack','Rose'],
                                    index=['s01','s02','s03','s04']),
                   'Age':pd.Series([18,18,20],
                                   index=['s01','s02','s04'])})
print(df)

print(df.axes)
print(df.index)
print(df.columns)
print(df.dtypes)
print(df.empty)
print(df.ndim) # 2
print(df.size)
print(df.values)
print(df.head(2))
print(df.tail(2))


