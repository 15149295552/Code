'''
Series示例
'''
import numpy as np
import pandas as pd

data = [100,90,80,60]
s = pd.Series(data,index=['zs','ls','ww','sl'])
print(s)

#通过字典创建Series
data = {'s101':'zs','s102':'ls','s103':'ww'}
s = pd.Series(data)
print(s)

#通过标量创建Series
s = pd.Series(0.2,index=np.arange(10))
print(s)

#访问Series中的数据
print('='*30)

s = pd.Series([100,90,80,70],
              index=['zs','ls','ww','sl'])
#位置索引
print(s[0])
print(s[0:2])
print(s[[0,1,3]])
#标签索引
print(s['zs'])
print(s['zs':'ls']) #终止位置的索引也会拿到
print(s[['zs','ls','sl']])


print(s.values)
print(s.index)
print(s.ndim) #1
print(s.shape) #(4,)
print(s.size) #4
print(s.dtype) #int64



