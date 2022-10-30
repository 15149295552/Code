# 循环嵌套
# 分类：while循环嵌套/for循环嵌套

# 需求：打印4行4列的星星（*）
# * * * *
# * * * *
# * * * *
# * * * *

# 分析：打印1行的星星，让循环进行4次
# 打印1行4列的星星
# i = 0
# while i < 4:
#     print('*', end=' ')
#     i += 1
# print()
#
# i = 0
# while i < 4:
#     print('*', end=' ')
#     i += 1
# print()
#
# i = 0
# while i < 4:
#     print('*', end=' ')
#     i += 1
# print()
#
# i = 0
# while i < 4:
#     print('*', end=' ')
#     i += 1
# print()

# 核心：循环做什么
x = 0
while x < 4:
    # 打印1行4列的星星
    i = 0
    while i < 4:
        print('*', end=' ')
        i += 1
    print()

    x += 1
# for i in range(4):  # 外层循环
#     # 外层循环的循环体
#     for j in range(4):   # 内层循环
#         # 内层循环的循环体
#         print('*', end=' ')
#     print()

'''
    while循环
        初始条件      循环条件      变化条件
        x=1          x < 21       x += 1
    
    for 循环（range函数）
        起始值        终止值        步长
        start=1      stop=21      step=1
'''







