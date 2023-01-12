"""
    函数式编程思想
        适用性：多个函数,主体结构相同,但是核心算法不同
        步骤：
            1. 分:将不同的算法单独定义在函数中
            2. 隔:使用参数隔离通用函数与变化函数
        价值：
            创造通用函数
"""
list01 = [3, 443, 54, 6, 7, 7]

# 定义函数,查找第一个大于10的数字
def first01():
    for item in list01:
        if item > 10:
            return item

# 定义函数,查找第一个小于100的数字
def first02():
    for item in list01:
        if item < 100:
            return item

print(first02())


# 变化函数(回调函数)
def condition01(item):
    return item > 10

def condition02(item):
    return item < 100

# 通用函数
def first(condition):
    for item in list01:
        if condition(item):
            return item


print(first(condition02))
print(first(condition01))

print(int(input()))



