'''
自定义复合类型
列与列之间类型可以不同,在同一列内,类型必须相同
'''
import numpy as np

data = [('zs',[100,100,100],18),
        ('ls',[90,90,90],19),
        ('ww',[80,80,80],20)]

# ary = np.array(data,dtype='U2,3int32,int32')
# print(ary)
# print(ary['f2'].mean())
# print(ary['f1'].mean(axis=0))

ary = np.array(data,dtype={'names':['name','score','age'],
                           'formats':['U2','3int32','int32']})
print(ary)
print(ary['age'].mean())







