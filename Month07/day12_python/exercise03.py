"""
    在common/iterable_tools模块中定义IterableHelper类
    添加first、find_all静态方法
    实现下列功能：
       在列表中查找所有偶数
       在列表中查找所有被4或7整除的数字
       查找第一个大于10的数字
       查找第一个小于100的数字
"""
from common.iterable_tools import IterableHelper

list01 = [3, 443, 54, 6, 7, 7]


def condition01(item):
    return item > 10


def condition02(item):
    return item < 100


def condition03(item):
    return item % 2 == 0


def condition04(number):
    return number % 4 == 0 or number % 7 == 0


print(IterableHelper.find_all(list01, condition03))
print(IterableHelper.find_all(list01, condition04))
print(IterableHelper.first(list01, condition01))
print(IterableHelper.first(list01, condition02))
