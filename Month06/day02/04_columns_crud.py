'''
dataframe列级操作
'''
import numpy as np
import pandas as pd

data = {'one':pd.Series([1,2,3],index=['a','b','c']),
        'two':pd.Series([1,2,3,4],index=['a','b','c','d']),
        'three':pd.Series([1,3,4],index=['a','c','d'])}
df = pd.DataFrame(data)
print(df)

#列的访问
print(df['two']) #列级索引只有标签索引,没有位置索引
# 列级访问,只能索引,不能切片
print(df[['one','two']])

#列的添加
#列的值为列表时,保证长度和原数据一致
df['four'] = [4,3,2,1]
#如果长度不一致,值设定为Series,
#如果为Series,index要和原始数据一致
df['five'] = pd.Series([1,2,3],
                       index=['a','b','c'])
print(df)


#列的删除
#删除一列
#del
del df['five']
print(df)

#pop
df.pop('four')
print(df)

#删除多列 axis=1 在水平轴向上找索引,才是列级索引
# inplace=False
df.drop(['one','three'],axis=1,inplace=True)
print(df)







