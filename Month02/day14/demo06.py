"""
    内置生成器函数
"""
list01 = [34, 4, 45, 5, 76]
# 读取全部元素
for item in list01:
    if item > 10:
        print(item)

# 修改全部元素
for i in range(len(list01)):
    if list01[i] > 10:
        list01[i] = 0

# 同时读取与修改元素
# item 是元组 (索引,元素)
# for item in enumerate(list01):
#     if item[1] > 10:
#         list01[item[0]] = 0
for i,item in enumerate(list01):
    if item > 10:
        list01[i] = 0

# 练习1：将列表中所有奇数设置为None
# 练习2：将列表中所有偶数自增1