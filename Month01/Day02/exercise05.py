'''
练习1:
    在终端中输入整数，打印是正数、负数、零

分析：
    1 获取输入的整数
    2 对整数进行判断
        == 0: 零
        > 0: 正数
        < 0: 负数
'''

number = int(input('请输入一个数：'))

if number == 0:
    print('零')
elif number > 0:
    print('正数')
else:
    print('负数')


# 方式2：if语句结构属于独立的判断，需要被多次执行，增加了程序执行的步数（不推荐）
number = int(input('请输入一个数：'))

if number == 0:
    print('零')
if number > 0:
    print('正数')
if number < 0:
    print('负数')