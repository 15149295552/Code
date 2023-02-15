
import numpy as np

#shape
ary = np.arange(1,9)
print(ary)
print(ary.shape)
#对shape属性进行元组赋值，修改数组的shape
ary.shape = (2,4)
print(ary)

ary.shape = (2,2,2)
print(ary)

print('===' * 20)

#dtype
ary = np.arange(1,9)
print(ary)
print(ary.dtype)

ary = ary.astype('float32')
print(ary)
print(ary.dtype)

#size
print('==' * 30)

ary = np.arange(1,9)
print(ary)
print(ary.size)
print(len(ary))

ary.shape = (2,4)
print(ary.size) #8
print(len(ary)) #2

#index索引
print('==' * 20)
ary = np.arange(1,9)
ary.shape = (2,2,2)

#三维数组[页，行，列]
#二维数组[行，列]
# print(ary[0][0][0])
# print(ary[0,0,0])

#通过索引的方式，拿到三维数组中的每个元素
#(2,2,2)
for i in range(ary.shape[0]):
    for j in range(ary.shape[1]):
        for k in range(ary.shape[2]):
            print(ary[i,j,k])




