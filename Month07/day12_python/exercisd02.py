"""
    需求：
    定义函数，在列表中查找所有偶数
    定义函数，在列表中查找所有被4或7整除的数字
    提示：满足条件的元素存入列表
    步骤：
        -- 根据需求，写出函数。
        -- 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数find_all
        -- 在当前模块中调用
"""
list01 = [6, 4, 49, 6, 7, 28, 89]


def find_all01():
    list_result = []
    for item in list01:
        if item % 2 == 0:
            list_result.append(item)
    return list_result


def find_all02():
    list_result = []
    for item in list01:
        if item % 4 == 0 or item % 7 == 0:
            list_result.append(item)
    return list_result


print(find_all02())

def condition01(item):
    return item % 2 == 0

def condition02(number):
    return number % 4 == 0 or number % 7 == 0

def find_all(condition):
    list_result = []
    for item in list01:
        # if item % 4 == 0 or item % 7 == 0:
        # if condition02(item):
        # if condition01(item):
        if condition(item):
            list_result.append(item)
    return list_result

print(find_all(condition01))
print(find_all(condition02))
