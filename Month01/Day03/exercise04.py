'''
练习1：程序产生1个 1到100之间的随机数，玩家仅有3次猜测机会，每次提示：大了、小了，同时打印剩余的机会数，如果3次机会内猜对，则打印恭喜您猜对了。

效果：
    请输入要猜的数字:80
    大了
    剩余 2 次机会
    请输入要猜的数字:62
    小了
    剩余 1 次机会
    请输入要猜的数字:66
    恭喜您猜对了

分析：
    1、生成：[1, 100] 之间的整数（rand_number）
    2、循环：
        1、输入一个数(user_number)
        2、比较
            user_number > rand_number: '大了'
            user_number < rand_number: '小了'
            user_number == rand_number: '猜对了' --> break
    3、记录次数
        for循环：循环3次，range(3, 0)
            打印剩余次数：打印变量
'''

import random

rand_number = random.randint(1, 100)   # 生产：[1, 100]
print(rand_number)

for i in range(3, 0, -1):
    user_number = int(input('请输入一个整数：'))
    if user_number > rand_number:
        print('大了')
    elif user_number < rand_number:
        print('小了')
    else:  # user_number == rand_number:
        print('猜对了')
        break

    i -= 1
    if i != 0:
        print('剩余的机会数：', i)