"""
    lambda应用
        作为函数的实参
            通用函数(可迭代对象,lambda表达式)
"""
from common.iterable_tools import IterableHelper

list01 = [3, 443, 54, 6, 7, 7]

# condition01与first紧耦合
# def condition01(item):
#     return item > 10

# print(IterableHelper.first(list01, condition01))

print(IterableHelper.first(list01, lambda item: item > 10))
print(IterableHelper.find_all(list01, lambda item: item < 100))
