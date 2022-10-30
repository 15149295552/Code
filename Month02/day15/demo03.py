"""
    函数式编程
        理论支柱：
            函数可以赋值给变量
"""


def func01():
    print("func01执行了")


func01()  # 直接调用
# a = func01() # 给变量赋值的是返回值
a = func01  # 函数没执行
a()  # 间接调用:通过变量调用函数，而不是函数名称


def func02():
    print("func02执行了")


def func03(func):
    print("func03执行了")
    # func02() # 直接调用:限定死了03与02的搭配
    func()  # 间接调用:03与"任何"函数搭配

def func04(p):
    print("func04执行了")

# func03(func04) #  因为间接调用时,没参数,所以func04无法传入
func03(func02)  #
func03(func01)  #

int(input())