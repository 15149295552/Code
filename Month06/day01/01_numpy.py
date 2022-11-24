'''
numpy中,数组的创建
'''
import numpy as np

#array
ary = np.array([1,2,3,4,5,6])
# print(ary)
# print(type(ary))

# print(ary * 2)
# print(ary == 3)
# print(ary + ary)
# print(ary * ary)

ary = np.array([[1,2,3],
                [4,5,6]])
# print(ary)


#arange(能够生成浮点数)
ary = np.arange(0,1.1,0.1)
# print(ary)


#zeros
ary = np.zeros(10,dtype='int32')
ary = np.zeros((3,3),dtype='int32')
ary = np.zeros((2,2,2),dtype='int32')
# print(ary)


#ones
ary = np.ones(10,dtype='bool_')
print(ary)

