"""
需求：
定义函数，在列表中查找第一个奇数
定义函数，在列表中查找第一个能被3或5整除的数字
步骤：
    -- 根据需求，写出函数。
    -- 因为主体逻辑相同,核心算法不同.
       所以使用函数式编程思想(分、隔、做)
       创建通用函数first
    -- 在当前模块中调用
"""
list01 = [6, 4, 53, 6, 7, 8, 89]

def first01():
    for item in list01:
        if item % 2 == 1:
            return item

def first02():
    for item in list01:
        if item % 3 == 0 or item % 5 == 0:
            return item

print(first02())

def condition01(item):
    return item % 2 == 1

def condition02(item):
    return item % 3 == 0 or item % 5 == 0

def first(condition):
    for item in list01:
        # if item % 2 == 1:
        # if condition01(item):
        # if condition02(item):
        if condition(item):
            return item

# 批量操作
print(first(condition01))