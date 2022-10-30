"""
    找出最有钱的员工
    找出编号最大的员工
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
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1001, 9002, "师父", 60000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

"""
def get_max01():
    max_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if max_value.money < list_employees[i].money:
            max_value = list_employees[i]
    return max_value

def get_max02():
    max_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if max_value.eid < list_employees[i].eid:
            max_value = list_employees[i]
    return max_value

print(get_max01())
print(get_max02())


def get_max(condition):
    max_value = list_employees[0]
    for i in range(1, len(list_employees)):
        # if max_value.eid < list_employees[i].eid:
        # if max_value.money < list_employees[i].money:
        if condition(max_value) < condition(list_employees[i]):
            max_value = list_employees[i]
    return max_value

print(get_max(lambda e:e.eid))
print(get_max(lambda e:e.money))
"""

print(IterableHelper.get_max(list_employees, lambda e: e.money))