# 作用域 scope

# # 全局作用域：变量可用于函数内外
# a = 10
#
# def func():
#     # 局部作用域：变量只能用在函数内部
#     b = 20
#     print(a, b)
#
# func()   # 函数执行结束后，栈帧被释放（存在的变量被销毁）
# print(a)

# 内建模块作用域在执行语句时，会预先加载，属于最大的作用域，当此作用域中无查找的内容时，则会产生错误


# 全局作用域：变量可用于函数内外
def func(x, y):
    # 局部作用域：变量只能用在函数内部
    b = 20
    y.append(x)
    print(x, y)

# a = 10
# b = [20, 30]
# func(a, b)    # 可变数据类型在函数内可以被修改，不可变数据类型在函数内不能被直接修改
# print(a, b)


# 全局的不可变数据类型在函数内被修改
def func(x, b):
    # 局部作用域：变量只能用在函数内部
    # global a   # 将局部作用域中的变量声明为全局作用域中的变量
    # global a, b   # global声明的变量不能出现在形参列表
    # global lists    # 可变数据类型可以不用在函数内部声明（被修改）
    a = 20
    b.append(x)
    print(x, b)

a = 10
lists = [20, 30]
func(a, lists)    # 可变数据类型在函数内可以被修改，不可变数据类型在函数内不能被直接修改
# print(a, b)