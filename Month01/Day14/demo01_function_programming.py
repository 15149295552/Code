# 函数式编程 function programming

# - 函数可以赋值给变量，赋值后变量绑定函数。
def func1():
    print('当前函数是:', func1.__name__)

# func1()
# print(func1)
# f = func1
# print(f)
# f()

# - 允许将函数作为参数传入另一个函数。
def func2():
    print('这是func2函数')

def func3(f):  # f = func2
    print('这是func3函数')
    f()  # func2()

# func3(func2)


# 函数式编程

list01 = [342, 4, 54, 56, 6776]

# 1 根据需求定义函数
# 需求1: 从列表查找出所有的大于100的数
def find01():
    for item in list01:
        if item > 100:
            yield item

# print(list(find01()))

# 需求2: 从列表查找出所有的偶数
def find02():
    for item in list01:
        if item % 2 == 0:
            yield item

# print(list(find02()))


# 2 提取变化点(条件)为函数   "封装 --> 分解"
def condition01(item):
    return item > 100

def condition02(item):
    return item % 2 == 0


# 3 定义通用结构函数
def find_all(condition):   # "继承 --> 隔离变化点"
    for item in list01:
        # if condition01(item):    # 不灵活
        # if condition02(item):
        if condition(item):  # "统一行为"
            yield item

# 4 调用函数实现需求
print(list(find_all(condition01)))   # "多态 --> 呈现不同的结果"
print(list(find_all(condition02)))
