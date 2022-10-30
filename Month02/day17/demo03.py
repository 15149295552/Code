"""
    装饰器 - 推导过程
        为旧功能增加新功能时,不修改旧功能代码

       有外有内:外函数负责接收旧功能
               内函数负责包装新旧功能
       内使用外:希望新旧功能同时执行
       外返回内:可以根据需求反复调用内函数
"""

"""
def old_func01():
    print("旧功能1")

def new_func():
    print("新功能")

# 新功能覆盖了旧功能
old_func01 = new_func 

old_func01()
"""

"""
def old_func01():
    print("旧功能1")

def new_func(func):
    print("新功能")
    func() # 执行旧功能

# 本行代码同时执行了新+旧
old_func01 = new_func(old_func01)
# 原来调用旧功能的代码报错(旧功能成为了None)
old_func01()
old_func01()
old_func01() 
"""


def old_func01():
    print("旧功能1")

def new_func(func):
    def wrapper():
        print("新功能")
        func()  # 执行旧功能
    return wrapper

old_func01 = new_func(old_func01)
old_func01()
old_func01()
old_func01()
