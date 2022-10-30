"""
    变量交换
        a,b=b,a
    计算最值
        min_value = list01[0]
        for i in range(1,len(list01)):
            if min_value > list01[i]:
                min_value = list01[i]
        print(min_value)
    排序
        升序排列：小 -> 大
        降序排列：大 -> 小
"""
list01 = [34, 45, 5, 65, 76, 87, 9]
"""
# 假设第一个最小值
min_value = list01[0]
# 从第二个开始到最后
# for item in list01[1:]: # 会触发浅拷贝
for i in range(1,len(list01)):
    # 使用最小值 与 后面比较
    if min_value > list01[i]:
        # 如果后面更小,则替换
        min_value = list01[i]
print(min_value)
"""
# 丢失数据
# for i in range(1,len(list01)):
#     if list01[0]  > list01[i]:
#         list01[0]  = list01[i]
# print(list01 )


"""
# 第一个元素是最小值
for i in range(1,len(list01)):
    if list01[0]  > list01[i]:
        list01[0],list01[i] = list01[i],list01[0]
print(list01 )

# [5, 45, 34, 65, 76, 87, 9]
# 第二个元素是最小值
for i in range(2,len(list01)):
    if list01[1]  > list01[i]:
        list01[1],list01[i] = list01[i],list01[1]
print(list01 )

# [5, 9, 45, 65, 76, 87, 34]
# 第三个元素是最小值
for i in range(3,len(list01)):
    if list01[2]  > list01[i]:
        list01[2],list01[i] = list01[i],list01[2]
print(list01 )
# [5, 9, 34, 65, 76, 87, 45]
# 第倒数第二个个元素是最小值
"""
# 取元素
for r in range(len(list01) - 1):
    # 作比较
    for c in range(r + 1, len(list01)):
        # 找更小
        if list01[r] > list01[c]:
            # 则交换
            list01[r], list01[c] = list01[c], list01[r]
print(list01)
