'''
dataframe的行级操作
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

#行级的访问,不能直接索引,能直接切片
#行级索引,既有位置索引,也有标签索引
# print(df['a':'b'])
# print(df[0:1])
# 只要是对行进行访问,都加上loc,或者iloc,就可以索引和切片了
print(df.loc['a'])
print(df.loc['a':'c'])
print(df.loc[['a','d']])

print(df.iloc[0])
print(df.iloc[0:2])
print(df.iloc[[0,3]])

print(df)

# 输入数据,所有行,不要最后一列(输入数据为二维数据)
x = df.iloc[:,:-1]
print(x)
# 输出数据,所有行,只要最后一列(输出数据为一维数据)
y = df.iloc[:,-1]
print(y)

#行的添加
df = pd.DataFrame([['zs',18],
                   ['ls',19]],
                  columns=['Name','Age'])
df2 = pd.DataFrame([['ww',20],
                    ['sl',21]],
                   columns=['Name','Age'])
# print(df)
# print(df2)
df = df.append(df2)
df.index = np.arange(4)
print(df)

#行的删除
df = df.drop([0,2],axis=0)
print(df)

#修改(通过列找行)

# 通过列找行,找到对应元素,进行赋值
df['Age'][1] = 20
print(df)
# 通过行找列,找到对应元素,进行赋值(修改不了)
df.loc[1]['Age'] = 666
print(df)





