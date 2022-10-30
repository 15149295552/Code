"""
    lambda 表达式
        匿名函数
            lambda 参数:函数体
            lambda能实现的功能def都能实现
            但是lambda只能有1句话且不能赋值
"""
# 1.有参数有返回值
# def func01(p1,p2):
#     return p1 > p2
#
#
# print(func01(5, 8))


func01 = lambda p1,p2: p1 > p2
print(func01(5, 8))

# 2.无参数有返回值
# def func02():
#     return 100
#
#
# print(func02())


func02 = lambda :100
print(func02())

# 3. 有参数无返回值
# def func03(p1):
#     print("参数是：",p1)
#
# func03(10)

func03 = lambda p1:print("参数是：",p1)
func03(10)

# 4. 无参数无返回值
# def func04():
#     print("hello world")
#
#
# func04()

func04 = lambda :print("hello world")
func04()

# 注意1:lambda函数体只能有一条语句
def func05():
    for number in range(10):
        print(number)

func05()

# lambda :for number in range(10):
#     print(number)

# 注意2:lambda 不能赋值
def func06(p1):
    p1[0] = 20

list01 = [10]
func06(list01)
print(list01) # [20]


# lambda p1:p1[0] = 20