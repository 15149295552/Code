"""
    定义函数,根据薪资对员工列表升序排列
    定义函数,根据部门对员工列表升序排列
    步骤：order_by
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
def order_by01():
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            if list_employees[r].money > list_employees[c].money:
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]

def order_by02():
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            if list_employees[r].did > list_employees[c].did:
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]

order_by01()
print(list_employees)

def order_by(condition):
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            if condition(list_employees[r]) > condition(list_employees[c]):
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]

order_by(lambda item:item.did)
print(list_employees)
"""

IterableHelper.order_by(list_employees,lambda e:e.money)
print(list_employees)

