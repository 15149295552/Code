# 99乘法表

'''
    行（乘数）：外层循环（1, 10）  i
    列（被乘数）：内层循环（1, 行号+1） j
        式子：j * i = i*j
'''
# 正乘法表
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(j, '*', i, '=', i * j, end='\t')
#     print()

# 倒乘法表
# print('-' * 50)
# for i in range(9, 0, -1):
#     for j in range(1, i + 1):
#         print(j, '*', i, '=', i * j, end='\t')
#     print()


for i in range(1, 10):
    print(' ' * 12 * (10-i-1), end='')
    for j in range(1, i + 1):
        print(j, '*', i, '=', i * j, end='\t')
    print()
# import random
#
# a = random.randint(1, 33)
# while True:
#     numb = random.randint(1, 33)
#     if numb != a:
#         b = numb
#         break
# while True:
#     numc = random.randint(1, 33)
#     if numc != a and numc != b:
#         c = numc
#         break
# while True:
#     numd = random.randint(1, 33)
#     if numd != a and numd != b and numd != c:
#         d = numd
#         break
# while True:
#     nume = random.randint(1, 33)
#     if nume != a and nume != b and nume != c and nume != d:
#         e = nume
#         break
# while True:
#     numf = random.randint(1, 33)
#     if numf != a and numf != b and numf != c and numf != d and numf != e:
#         f = numf
#         break
# list01 = [a, b, c, d, e, f]
# list01.sort()
# print(f'红球为{list01}，蓝球为{random.randint(1, 16)}')
# import random
#
# list02 = []
# while True:
#     s = random.randint(1, 33)
#     if s in list02:
#         continue
#     else:
#         list02.append(s)
#         list02.sort()
#     if len(list02) == 6:
#         break
# list02.append(random.randint(1, 16))
# print(list02)
# '''分析：
#         浮点数特点：
#             1 只能有一个小数点
#             2 除了小数点外全都是数字
# '''
# # data = input('请输入一个数：')
# # if data.count('.') == 1 and data.replace('.', '').isdigit():
# #     print(True)
# # else:
# #     print(False)
# import random
#
# list_ball = []
# while True:
#     red_ball = random.randint(1, 33)
#     if red_ball not in list_ball:
#         list_ball.append(red_ball)
#     if len(list_ball) == 6:
#         break
# list_ball.sort()
# blue_ball = random.randint(1, 16)
# list_ball.append(blue_ball)
# print(list_ball)
