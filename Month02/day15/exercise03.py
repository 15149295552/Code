"""
    在common/iterable_helper/IterableHelper类中
    定义静态的高阶函数实现下列功能:
"""
# -- 在列表中查找第一个能被8整除的数字
# -- 在列表中查找第一个个位是奇数的数字
# -- 在字典中查找第一个值是20的键
# -- 在字典中查找第一个值是奇数的键
from common.iterable_tools import IterableHelper

list01 = [54, 5, 65, 16, 87]
dict01 = {"a":10,"b":20,"c":30}

def condtion01(p1):
    return p1 % 8 ==0

def condition02(item):
    return item % 2 !=0

def condition03(key):
    return dict01[key] == 20

def condition04(key):
    return dict01[key] % 2 == 1

print(IterableHelper.find_single(list01, condtion01))
print(IterableHelper.find_single(list01, condition02))
print(IterableHelper.find_single(dict01, condition03))
print(IterableHelper.find_single(dict01, condition04))
