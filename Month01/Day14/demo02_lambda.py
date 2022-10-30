# lambda表达式

# 需求: 计算一个数的平方
def power(num):
    return num ** 2


# print(power(4))

# 有参数有返回值
power = lambda num: num ** 2
# print(power)
print(power(4))
#
# print((lambda num: num ** 2)(4))   # 不推荐


# 有参数无返回值
func2 = lambda num: print(num)
func2(666)
# print(func2(666))

# 无参数有返回值
func3 = lambda: 'OK'
print(func3())

# 无参数无返回值
func4 = lambda: print(777)
func4()

# 注意
# 方法体只能有一条语句
# func5 = lambda num: print(1);print(num)
# func5(6)

# 不支持赋值语句。
# func6 = lambda a, b: a, b = b, a
# func6(3, 2)