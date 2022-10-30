'''
定义函数实现以下场景：
（2）限定3次机会，用户循环输入指定范围的数，如果输入数大于随机数，则提示
输入过大；如果输入数小于随机数，则提示输入过小；否则提示恭喜你猜对了或次
数用完，退出猜数；如果是次数用完猜对则打印您的账号被锁定。

分析:
    0 定义函数: guess_number()
    1 导入随机模块,生成1-100之间的随机整数
    2 定义变量记录次数
    3 循环录入(判断次数)
        1 输入猜测的整数, 输入一次,次数-1
        2 判断用户输入的数与随机数的大小关系
            大了: print('大了')
            小了: print('小了')
            相等: print('猜对了, 共用xxx次机会')
                break
        3 打印剩余的次数
    4 循环结束(循环条件不成立)
        print('您的账号被锁定')
'''
import random

num = random.randint(1, 100)

def guess_number():
    index = 0
    while index < 3:
        num_01 = int(input('请输入一个整数'))
        index += 1
        if num_01 > num:
            print('您输入的数字大了')
        elif num_01 < num:
            print('您输入的数字小了')
        else:
            print(f'猜对了, 共用{index}次机会')
            break

        if index < 3:
            print(f'您还剩余{3 - index}次')
    else:
        print('您的账号被锁定了')

guess_number()
