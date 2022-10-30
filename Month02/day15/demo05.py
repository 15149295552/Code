"""
     将通用函数定义在IterableHelper类中
"""
from common.iterable_tools import IterableHelper

list01 = [5, 5, 56, 6, 78]

def condition01(item):
    return item > 50

def condition02(item):
    return item % 3 == 0

def condition03(number):
    return number < 10

print(IterableHelper.find_single(list01,condition01))
print(IterableHelper.find_single(list01,condition02))
print(IterableHelper.find_single(list01,condition03))
