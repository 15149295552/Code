"""
    闭包
        字面意思:封闭 外部函数栈帧
        作用：外部函数栈帧执行过后不释放,
             供内部函数使用
        三大要素:
            有外有内
            内使用外
            外返回内
"""


def func01():  # 午饭
    a = 100  # 100道菜

    def func02():  # 晚饭
        print(a)  # 吃剩菜

    # return func02() # 执行func02,返回None
    return func02


# 调用外函数,接收内函数
result = func01()
# 反复执行内函数
result()  # 间接调用
result()  # 间接调用
result()  # 间接调用
result()  # 间接调用
