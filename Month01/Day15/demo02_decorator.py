# 装饰器 - decorator

# 前提: 不能改变原函数的调用/原函数内部代码
# def func01():
#     print('这是原函数01功能')
#
# def func02():
#     print('这是原函数02功能')

# def func():
#     '''  封装新功能+旧功能  '''
#     print('新功能')
#     # func01()   # 旧功能
#     func02()   # 旧功能

# 代码冗余
# def func():
#     '''  封装新功能+旧功能  '''
#     print('新功能')
#     func02()   # 旧功能

# def func(function):
#     '''  封装新功能+旧功能  '''
#     def inner():
#         print('新功能')
#         function()   # 旧功能
#     return inner

# f1 = func(func01)
# f1()
# f2 = func(func02)
# f2()

# func01 = func(func01)
# func01()


# 1 考虑原函数有参数
# def func01(number):
#     print('这是原函数01功能:', number)
#
# def func02():
#     print('这是原函数02功能')
#
# def func(function):    # function = func01
#     '''  封装新功能+旧功能  '''
#     def inner(*args, **kwargs):   # *args: 接收多个位置实参(元组)  **kwargs: 接收多个关键字实参(字典)
#         print('新功能')
#         function(*args, **kwargs)   # 旧功能  func01(*args)  --> 序列传参 (拆解序列,按照位置传递实参)
#                                     # 旧功能  func01(**kwargs)  --> 字典关键字传参 (拆解字典,按照关键字传递实参)
#     return inner
#
# f1 = func(func01)
# # f1(10)   # 位置传参
# # f1(20)     # 可能存在关键字传参
# f2 = func(func02)
# f2()

# 2 考虑原函数有返回值
# def func01(number):
#     print('这是原函数01功能:', number)
#
# def func02():
#     print('这是原函数02功能')
#     return 'OK'
#
# def func(function):
#     '''  封装新功能+旧功能  '''
#     def inner(*args, **kwargs):
#         print('新功能')
#         return function(*args, **kwargs)
#     return inner
#
# # f1 = func(func01)
# # print(f1(10))
# # f2 = func(func02)
# # result2 = f2()
# # print(result2)
#
# # 不改变原函数的调用
# func01 = func(func01)
# func01(20)
# func02 = func(func02)
# print(func02())


# 终极写法
# 装饰器函数
def func(function):
    '''  封装新功能+旧功能  '''
    def inner(*args, **kwargs):
        print('新功能')
        return function(*args, **kwargs)
    return inner

@func    # func01 = func(func01)
def func01(number):
    print('这是原函数01功能:', number)

@func    # func02 = func(func02)
def func02():
    print('这是原函数02功能')
    return 'OK'

func01(20)
print(func02())