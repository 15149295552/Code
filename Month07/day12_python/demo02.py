"""
    函数式编程理论支柱：
        函数可以赋值给变量
"""


def func01():
    print("func01")

def func02():
    print("func02")

def func03(func):
    print("func03")
    # func02() # 直接调用:固定搭配
    func() # 间接调用:灵活搭配

func01()  # 直接调用
# a = func01()  # 将返回值赋值给a(执行函数)
a = func01 # 将函数地址交给变量a(不执行函数)
a() # 间接调用

func03(func02)
func03(func01)