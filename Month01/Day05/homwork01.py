'''
2 面试题：判断输入的字符串是一个浮点数，并打印判断的结果（True/False)?
3 作业：使用程序实现打印一注双色球
     红球：6个（1-33（包含）之间的整数）-不重复（排序升序）
     篮球：1个（1-16（包含）之间的整数）
'''

# 2 面试题：判断输入的字符串是一个浮点数，并打印判断的结果（True/False)?
''' 分析：
        浮点数特点：
            1 只能有一个小数点
            2 除了小数点外全部是数字
'''

# data = input('请输入一个数：')
#
# if data.count('.') == 1 and data.replace('.', '').isdigit():
#     print(True)
# else:
#     print(False)

'''
使用程序实现打印一注双色球
     红球：6个（1-33（包含）之间的整数）-不重复（排序升序）
     篮球：1个（1-16（包含）之间的整数）
     
分析：
    0 导入random
    1 创建空列表
    2 循环：while True
        1 产生 [1, 33] 的随机整数
        2 判断：随机数是否在列表（不重复）
            不存在：添加至列表
        3 判断：列表长度是否等于6
            等于：break
    3 升序排列
    4 添加篮球
        1 产生 [1, 16] 的随机整数
        2 添加至列表
    5 打印列表
'''

import random

list_ball = []

while True:
    red_ball = random.randint(1, 33)
    if red_ball not in list_ball:
        list_ball.append(red_ball)

    if len(list_ball) == 6:
        break

list_ball.sort()

blue_ball = random.randint(1, 16)
list_ball.append(blue_ball)

print('彩票结果：', list_ball)