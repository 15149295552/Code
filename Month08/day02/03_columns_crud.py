'''
对于Dataframe的列级操作
'''
import numpy as np
import pandas as pd

data = {'one':pd.Series([1,2,3],index=['a','b','c']),
        'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
        'three':pd.Series([1,3,4],index=['a','c','d'])}

df = pd.DataFrame(data)
print(df)

#访问(列级索引，没有位置索引)
print(df['one']) #访问一列直接索引列名
#访问多列不能切片,可以使用掩码
print(df[['one','two']])
#不要最后一列
print(df[df.columns[:-1]])

#列的添加  df[列名] = 列数据
#值为列表时，需要保证当前列的元素个数和行级索引数量一致
df['four'] = [1,2,3,4]
print(df)

#如果值为Series，要保证index和原始数据的index一致
df['five'] = pd.Series([1,2,3],
                       index=['a','b','c'])
print(df)


#列的删除
del df['five']
print(df)

df.pop('four')
print(df)

df.drop(['three','two'],axis=1,inplace=True)
print(df)















