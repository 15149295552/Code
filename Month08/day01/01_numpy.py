'''
ndarray数组的创建
'''
import numpy as np

ary = np.array([1,2,3,4,5,6])
# print(ary)
# print(type(ary))
# print(ary * 2)
# print(ary + 2)
# print(ary == 3)
# print(ary + ary)
# print(ary * ary)

ary = np.arange(0.1,1.1,0.1)
# print(ary)

#如果不指定dtype，默认为float64
ary = np.zeros(10)
print(ary)

ones = np.ones((3,3),dtype='int32')
print(ones)

zeros_like = np.zeros_like(ones)
print(zeros_like)

#从-π到+π，生成200个数
#线性拆分(起始位置,终止位置，个数) 包含终止位置
ary = np.linspace(-np.pi,np.pi,200)
print(ary)
print(len(ary))

ary = np.linspace(0.1,1,10)
print(ary)




