"""
    练习3：
    需求：
    定义函数，在员工列表中查找所有部门是9002的员工数量
    定义函数，在员工列表中查找所有员工编号大于1002的员工工数量
    步骤：
       -- 根据需求，写出函数。
       -- 因为主体逻辑相同,核心算法不同.
          所以使用函数式编程思想(分、隔、做)
          创建通用函数get_count
       -- 在当前模块中调用
"""
from common.iterable_tools import IterableHelper


class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

    def __str__(self):
        return str(self.__dict__)


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]


def get_count01():
    count = 0
    for item in list_employees:
        if item.did == 9002:
            count += 1
    return count


def get_count02():
    count = 0
    for item in list_employees:
        if item.eid > 1002:
            count += 1
    return count


print(get_count01())


def condition01(item):
    return item.did == 9002


def condition02(item):
    return item.eid > 1002


def get_count(condition):
    count = 0
    for item in list_employees:
        # if item.did == 9002:
        # if condition01(item):
        # if condition02(item):
        if condition(item):
            count += 1
    return count

print(get_count(condition01))

print(IterableHelper.get_count(list_employees, condition01))
