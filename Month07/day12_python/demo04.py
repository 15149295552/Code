"""
    函数式编程思想
"""
from common.iterable_tools import IterableHelper

list01 = [3, 443, 54, 6, 7, 7]


def condition01(item):
    return item > 10


def condition02(item):
    return item < 100


print(IterableHelper.first(list01, condition01))
