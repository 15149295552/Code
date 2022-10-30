# 用户输入数，打印 xx 是（不是）素数
# 素数：因数只有1与本身的数（因数 * 因数 = 积）
# 如：2 3 5 7 11

# 方法1: 通过循环记录因数的个数
# number = 8
# count = 0
# if number > 1:
#     for i in range(1, number+1):
#         if number % i == 0:
#             count += 1
#
#     if count > 2:
#         print(number, '不是素数')
#     elif count == 2:
#         print(number, '是素数')
# else:
#     print('输入的数错误')


# 方法2：
''' 思路：
    计算的数：8
        寻找 2 - 8 之间是否还存在第3个因数
            8 % 2/3/4/5/6/7 == 0
        存在为0：不是素数
        不存在为0：是素数
'''

number = int(input('请输入一个整数：'))

if number > 1:
    for x in range(2, number):
        if number % x == 0:
            print(number, '不是素数')
            break
    else:
        print(number, '是素数')
else:
    print('输入的数错误')