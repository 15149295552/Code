'''
数据的一些基本的属性
'''
import numpy as np

ary = np.arange(1, 9)
print(ary)
print(ary.shape)
# ary.shape是一个元祖,可以直接进行元祖赋值,修改维度
ary.shape = (2, 4)
print(ary)
print(ary.shape)
print('-' * 30)

ary.shape = (2, 2, 2)
print(ary)
print(ary.shape)

print('=' * 30)
# dtype
ary = np.arange(1, 10)
print(ary)
print(ary.dtype)
# ary.dtype = 'float64' # 不会修改元素类型,只是修改了阅读方式
# print(ary)

ary = ary.astype('float64')
print(ary)
print(ary.dtype)

print('=' * 30)
ary = np.arange(1, 9)
ary.shape = (2, 2, 2)
print(ary)
print(ary.size)
print(len(ary))

print('=' * 20)

ary = np.arange(1, 9)
print(ary)
print(ary[0])
print(ary[-1])
ary.shape = (2, 2, 2)
print(ary)
print(ary[0][0][0])
print(ary[0, 0, 0])
# 三维: 数组[页,行,列]
# 二维: 数组[行,列]


print('=' * 30)
ary = np.arange(1, 9)
ary.shape = (2, 2, 2)

for i in range(ary.shape[0]):  # 拿到有几页
    for j in range(ary.shape[1]):  # 拿到有几行
        for k in range(ary.shape[2]):  # 拿到有几列
            print(ary[i, j, k])




