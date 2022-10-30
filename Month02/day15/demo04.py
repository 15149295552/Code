"""
    函数式编程思想
        适用性:多个函数主体结构相同,核心算法不同
        步骤：
            分:将不同的核心算法(变化点),单独定义在函数中
            隔:在通用函数中将核心算法抽象为参数,从而隔离通用函数与核心算法
            做:参照间接调用的方式,新增核心算法
"""
list01 = [5, 5, 56, 6, 78]


# 需求:定义函数,获取第一个大于50的数字
def find_single_gt_50():
    for item in list01:
        if item > 50:
            return item


# 需求:定义函数,获取第一个能被3整除的数字
def find_single_divisible_by_3():
    for item in list01:
        if item % 3 == 0:
            return item


def condition01(item):
    return item > 50


def condition02(item):
    return item % 3 == 0


# 通用函数:根据任意条件查找第一个元素
def find_single(condition):
    for item in list01:
        # if item > 50:
        # if condition01(item):
        # if condition02(item):
        if condition(item):  # 间接调用
            return item


# 增加新功能:小于10的数
def condition03(number):
    return number < 10


print(find_single(condition01))
print(find_single(condition02))
print(find_single(condition03))
