'''
对于dataframe的行级操作
'''
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

data = {'one':pd.Series([1,2,3],index=['a','b','c']),
        'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
        'three':pd.Series([1,3,4],index=['a','c','d'])}

df = pd.DataFrame(data)
print(df)

#行的访问
#不能直接索引
#对行进行操作，加上loc(标签) 或者iloc(位置)
print(df.loc['a'])
print(df.loc['a':'c'])
print(df.loc[['a','c','d']])

print(df.iloc[0])
print(df.iloc[:3])
print(df.iloc[[0,1,3]])

#行的添加 append
df = pd.DataFrame([['zs',18],['ls',20]],
                  columns=['Name','Age'])
df2 = pd.DataFrame([['Alex',28],['Linus',28]],
                   columns=['Name','Age'])
df = df.append(df2)
print(df)
df.index = [0,1,2,3]
print(df)

#删除
df.drop([1,2],axis=0,inplace=True)
print(df)

#修改
#通过列找行的方式，找到这个元素，对其进行赋值
df['Age'][0] = 666
print(df)
#通过行找列的方式，找到这个元素，对其进行赋值
#通过行找的方式，底层时没有赋值
# df.loc[0]['Age'] = 999
# print(df)

