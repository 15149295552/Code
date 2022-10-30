"""
    练习1： 让下列代码重复执行，输入y继续(不输入y则退出)
"""
while True:
    number = int(input("请输入数字："))
    if number > 0:
        print("正数")
    elif number < 0:
        print("负数")
    else:
        print("零")

    if input("请输入y键继续:") != "y":
        break
