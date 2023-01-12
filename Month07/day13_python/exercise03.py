"""
    需求：
        定义函数，在员工列表中累加所有员工薪资
        定义函数，在员工列表中累加所有员工编号
    步骤：
        -- 根据需求，写出函数。
        -- 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数
            -- 在当前模块中调用
"""
from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

"""
def sum01():
    value = 0
    for item in list_employees:
        value += item.money
    return value

def sum02():
    value = 0
    for item in list_employees:
        value += item.eid
    return value

print(sum02())

def condtion01(item):
    return item.money

def condtion02(item):
    return item.eid

#  电脑  -->  接口USB
#             麦克风  鼠标    游戏手柄  ...
def sum(condtion):
    value = 0
    for item in list_employees:
        # value += item.eid
        # value += condtion02(item)
        # value += condtion01(item)
        value += condtion(item) # 先确定用法
    return value

# lambda如何定义,取决于高阶函数内部的使用
print(sum(condtion01))
print(sum(lambda emp:emp.money)) # 后定义做法
"""

print(IterableHelper.sum(list_employees, lambda e: e.money))
print(IterableHelper.sum(list_employees, lambda e: e.eid))
print(IterableHelper.sum(list_employees, lambda e: e.did))