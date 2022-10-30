"""
    练习1:  在终端中输入整数、打印正数、 负数、零
"""
number = int(input("请输入数字："))
if number > 0:
    print("正数")
elif number < 0:
    print("负数") 
else:
    print("零")
