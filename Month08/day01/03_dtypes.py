'''
自定义复合类型
列于列之间可以为不同的类型，但同一列内类型必须相同
'''
import numpy as np
import warnings
warnings.filterwarnings('ignore')

data = [('zs',[100,100,100],18),
        ('ls',[90,90,90],19),
        ('ww',[80,80,80],20)]

#第一种：字符串
# ary = np.array(data,dtype='U2,3int32,int32')
# print(ary)
# print(ary['f2'].mean())
# print(ary[2][2])
# print(ary['f1'])

#第二种：字典
ary = np.array(data,dtype={'names':['name','score','age'],
                           'formats':['U2','3int32','int32']})

print(ary['score'].mean(axis=0))


