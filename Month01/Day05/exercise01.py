# 1、生成10--30之间能被3或者5整除的数字
# ​    [10, 12, 15, 18, 20, 21, 24, 25, 27]
# 常规方法
# list1 = []
#
# for i in range(10, 30):
#     if i % 3 == 0 or i % 5 == 0:
#         list1.append(i)
# print(list1)

# 推导式
# print([i for i in range(10, 30) if i % 3 == 0 or i % 5 == 0])


# 2、生成5 -- 20之间的数字平方
# ​    [25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
# # 常规方法
# list2 = []
#
# for i in range(5, 20):
#     list2.append(i ** 2)
# print(list2)
#
# # 推导式
# print([i ** 2 for i in range(5, 20)])


# 3、生成二维列表：[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# 常规方法
# list3 = []
#
# for i in range(3):   # 0 1 2
#     list4 = []
#     for x in range(i*4+1, i*4+5):
#         list4.append(x)
#     list3.append(list4)
#
# print(list3)
#
# # 推导式
# print([[x for x in range(i*4+1, i*4+5)] for i in range(3)])


list01 = list(range(10))
print(list01, id(list01))   # 3127598948160

for i in range(10000000):
    list01.append(i)
print(list01, id(list01))   # 3127598948160