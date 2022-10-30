# while循环

# 结构1：while语句
# print('跑圈')
# print('跑圈')
# print('跑圈')
# print('跑圈')
# print('跑圈')

# 计数器
# count = 0
# print('跑圈')
# count += 1
# print('跑圈')
# count += 1
# print('跑圈')
# count += 1
# print('跑圈')
# count += 1
# print('跑圈')
# count += 1
# print(count)

# count = 0  # 初始条件
#
# while count < 5:  # count: 0 1 2 3 4  循环条件
#     # 循环体：while后的条件成立（True），则执行
#     print('跑圈')
#     count += 1  # 变化条件
# print(count)


# 结构2：while-else语句
# count = 0  # 初始条件
#
# while count < 5:  # 循环条件
#     print('跑圈')
#     count += 1  # 变化条件
# else:  # 当while后的条件不成立（False）则执行 (count=5)
#     print('今天打卡完成，明天继续')


# count = 0  # 初始条件
#
# while count < 5:  # 循环条件
#     print('跑圈')
#     count += 1  # 变化条件
# print('今天打卡完成，明天继续')   # 此语句一定会执行


# 结构3：while+if语句
# 需求：打印1-10之间所有的偶数
# i = 1
# while i < 10:
#     if i % 2 == 0:
#         print(i, end=' ')
#     i += 1


i = 1
while i < 10:
    i += 1
    if i % 2 == 0:
        print(i, end=' ')
