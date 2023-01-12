"""
    需求：
        定义函数，在员工列表中查找所有员工姓名
        定义函数，在员工列表中查找所有员工工资
    步骤：
        -- 根据需求，写出函数。
        -- 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数select
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
def select01():
    list_result = []
    for item in list_employees:
        list_result.append(item.name)
    return list_result


def select02():
    list_result = []
    for item in list_employees:
        list_result.append(item.money)
    return list_result


print(select02())


def condition01(item): # 4
    return item.name

def condition02(item):
    return item.money

# 委托
def select(condition): # 2
    list_result = []
    for item in list_employees:
        # list_result.append(item.money)
        # list_result.append(condition02(item))
        # list_result.append(condition01(item))
        list_result.append(condition(item)) # 3
    return list_result


res1 = select(condition01) # 1
res2 = select(lambda e:e.eid) # 1
res2 = select(lambda e:(e.name,e.money)) # 1
print(res2)
"""

print(IterableHelper.select(list_employees, lambda e: e.did))
print(IterableHelper.select(list_employees, lambda e: [e.eid,e.name]))