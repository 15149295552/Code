"""
    定义函数,判断员工列表中是否存在姓名相同的员工
    定义函数,判断员工列表中是否存在薪资相同的员工
    步骤：
       -- 根据需求，写出函数。
       -- 因为主体逻辑相同,核心算法不同.
          所以使用函数式编程思想(分、隔、做)
          创建通用函数 is_repeat
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
def is_repeat01():
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            if list_employees[r].name == list_employees[c].name:
                return True
    return False


def is_repeat02():
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            if list_employees[r].money == list_employees[c].money:
                return True
    return False


print(is_repeat02())


def is_repeat(condition):
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            # if list_employees[r].money == list_employees[c].money:
            if condition(list_employees[r]) == condition(list_employees[c]):
                return True
    return False


print(is_repeat(lambda item: item.money))
"""

print(IterableHelper.is_repeat(list_employees, lambda item: item.money))
