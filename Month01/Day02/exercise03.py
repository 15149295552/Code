'''
练习：在终端中输入一个四位整数，计算每位相加和。
例如：录入1234，打印1+2+3+4结果

效果：
请输入四位整数：1234
结果是：10
'''
# # 方式1
# number = int(input('请输入一个四位数：'))
#
# thousand = number // 1000
# hundred = number // 100 % 10
# ten = number // 10 % 10
# one = number % 10
# # print(thousand, hundred, ten, one)
#
# result = thousand + hundred + ten + one
#
# print('计算的和为：', result)


# 方式2
number = int(input('请输入一个四位数：'))

result = number // 1000
result += number // 100 % 10
result += number // 10 % 10
result += number % 10

print('计算的和为：', result)