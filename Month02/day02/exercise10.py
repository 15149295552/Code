"""
    练习：在终端中输入一个四位整数，计算每位相加和。
    例如：录入1234，打印1+2+3+4结果
    效果：
    请输入四位整数：1234
    结果是：10
"""
# number = int(input("请输入四位整数:")) # 1234
# unit01 = number % 10 # 个位
# # number // 10  -> 123
# unit02 = number // 10 % 10
# unit03 = number // 100 % 10
# unit04 = number // 1000 # 千位
# result = unit01 + unit02 + unit03 +unit04
# print("结果是:"+str(result))

number = int(input("请输入四位整数:")) # 1234
result = number % 10
result += number // 10 % 10
result += number // 100 % 10
result += number // 1000
print("结果是:"+str(result))






