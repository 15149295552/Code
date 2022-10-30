'''
练习1：程序产生1个 1到100之间的随机数，让玩家重复猜测,直到猜对为止，每次提示：大了、小了、恭喜猜对了,总共猜了多少次。
效果：
    请输入要猜的数字:50
    大了
    请输入要猜的数字:25
    小了
    请输入要猜的数字:35
    大了
    请输入要猜的数字:30
    小了

    请输入要猜的数字:32
    恭喜猜对啦,总共猜了5次

分析：
    1 生产 1-100之间的随机整数
    2 循环：while True
        1 输入一个数
        2 判断该数与随机数的大小关系
            r > u: '小了'
            r < u: '大了'
            r == u: '猜对了' - break
    3 记录次数
        循环外：times = 0
        循环内：输入一次，times+=1
        最后，打印猜测的次数
'''

import random

rand_number = random.randint(1, 100)
times = 0

while True:
    user_number = int(input('请输入一个整数：'))
    times += 1
    if user_number > rand_number:
        print('大了')
    elif user_number < rand_number:
        print('小了')
    else:
        print('猜对了')
        break
    print('已经使用了：', times, '次机会')

print('共用了：', times, '次机会')