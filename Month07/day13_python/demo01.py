"""
    lambda
        匿名函数
            lambda 参数:函数体

        lambda可以实现的功能,def都可以;
        但是lambda只支持一条语句且不支持赋值
"""
# 1. 有参数有返回值
# def func01(p1,p2):
#     return p1 > p2
#
# print(func01(10, 20))

func01 = lambda p1, p2: p1 > p2
print(func01(10, 20))

# 2. 无参数有返回值
# def func02():
#     return 100
#
# print(func02())

func02 = lambda: 100
print(func02())

# 3. 有参数无返回值
# def func03(p1):
#     print("参数是%s" % p1)
#
# func03(10)

func03 = lambda p1: print("参数是%s" % p1)

func03(10)


# 4. 无参数无返回值
# def func04():
#     print("hello world")
#
# func04()

func04 = lambda :print("hello world")
func04()

# 5. lambda不支持赋值语句
def func05(p1):
    p1[0] = 100

list01 = [10]
func05(list01)
print(list01) # [100]

# lambda p1:p1[0] = 100

# 6.lambda函数体内只能有一条语句
def func06():
    for number in range(5):
        print(number)

func06()

# lambda :for number in range(5):
#     print(number)





