"""
    需求2：sum
    定义函数，累加所有员工薪资
    定义函数，累加所有员工编号
    步骤：
       -- 根据需求，写出函数。
       -- 因为主体逻辑相同,核心算法不同.
          所以使用函数式编程思想(隔、做)
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

    def __str__(self):
        return str(self.__dict__)

list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

"""
def sum01():
    sum_value = 0
    for item in list_employees:
        sum_value += item.money
    return sum_value

def sum02():
    sum_value = 0
    for item in list_employees:
        sum_value += item.eid
    return sum_value


def sum(condition):
    sum_value = 0
    for item in list_employees:
        # sum_value += item.money
        sum_value += condition(item)
    return sum_value


print(sum(lambda e: e.money))
"""

print(IterableHelper.sum(list_employees, lambda e: e.eid))

