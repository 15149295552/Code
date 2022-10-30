"""
    练习：
    在终端中获取一个整数，作为边长，打印矩形。
    效果：
    请输入整数:5
    $$$$$
    $   $
    $   $
    $   $
    $$$$$
"""
# number = int(input("请输入数字："))
# print("$" * number)
# for item in range(number-2):#0 1 2
#     print("$%s$" % (" " * (number - 2)))
# print("$" * number)

number = int(input("请输入数字："))
for item in range(number):  # 0 1 2 3 4
    # 如果头尾
    if item == 0 or item == number - 1:
        print("$" * number)
    else:# 否则
        print("$%s$" % (" " * (number - 2)))
