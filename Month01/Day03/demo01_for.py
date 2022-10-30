# for循环

# 结构1: for语句
# 遍历字符串：python 中每个字符
# for x in 'python':
#     print(x, end=' ')


# 结构2：for-else语句
# for x in 'python':
#     print(x, end=' ')
# else:  # 当可迭代对象中无数据时，则执行
#     print('字符遍历完毕')


# range函数：生产一组整数值的可迭代对象（iterable）
# 结构1：range(stop)
# stop: 表示终止值，不包含
# 需求：生成10以内的整数
# for i in range(10):
#     print(i, end=' ')

# 结构2：range(start, stop)
# start: 表示起始值，默认为0
# stop: 表示终止值，不包含
# 需求：生成2-10以间的整数
# for i in range(2, 10):
#     print(i, end=' ')


# 结构3：range(start, stop, step)
# start: 表示起始值，默认为0
# stop: 表示终止值，不包含
# step: 表示步长或偏移值，默认为1
#       正：表示正向取值（从小到大）
#       负：表示反向取值（从大到小）
# 需求：生成2-10以间的偶数
# for i in range(2, 10, 2):
#     print(i, end=' ')

# 需求：生成20-10以间的偶数
# for i in range(20, 10, -2):
#     print(i, end=' ')

# 注意：以下写法无法获取数据
# # 1 步长方向与取值反向相反
# for i in range(2, 10, -2):
#     print(i, end=' ')

# 2 起始值与终止值重合
for i in range(2, 2, -2):
    print(i, end=' ')