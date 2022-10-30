"""
    函数 - 参数
        调用函数 给 定义函数传递信息
        定义函数时,数据可以灵活
"""


def attack(count):  # 形式参数:假的,抽象
    for item in range(count):
        print("直拳")
        print("摆拳")
        print("勾拳")


attack(3)  # 实际参数:真的,具体
number = 5
attack(number)  # 传递的是数据地址,不是变量本身

