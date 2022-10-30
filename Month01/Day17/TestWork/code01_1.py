'''
1、猜数游戏
    定义函数实现以下场景：
    提示：产生随机整数
    （1）用户循环输入指定范围的数，如果输入数大于随机数，则提示输入过大；如果
    输入数小于随机数，则提示输入过小；否则提示恭喜你猜对了，退出猜数。

分析:
    0 定义函数: guess_number()
    1 导入随机模块,生成1-100之间的随机整数
    2 定义变量记录次数
    3 循环录入
        1 输入猜测的整数, 输入一次,次数＋1
        2 判断用户输入的数与随机数的大小关系
            大了: print('大了')
            小了: print('小了')
            相等: print('猜对了, 共用xxx次机会')
                break
'''
import random

def guess_number():
    rand_number = random.randint(1, 100)
    print(rand_number)
    times = 0
    while True:
        user_number = int(input('请输入一个整数:'))
        times += 1
        if user_number > rand_number:
            print('大了')
        elif user_number < rand_number:
            print('小了')
        # elif user_number == rand_number:
        else:
            print('猜对了')
            print('共用了', times, '次机会')
            break

guess_number()
