"""
    练习2：
    需求：
    定义函数，在员工列表中查找所有部门是9001的员工
    定义函数，在员工列表中查找所有姓名是2个字的员工
    步骤：
       -- 根据需求，写出函数。
       -- 因为主体逻辑相同,核心算法不同.
          所以使用函数式编程思想(分、隔、做)
          创建通用函数find_all
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

def find_all01():
    for item in list_employees:
        if item.did == 9001:
            yield item

def find_all02():
    for item in list_employees:
        if len(item.name) == 2:
            yield item

# 参数:列表中的元素
# 返回值:对列表元素的判断结果
def condition01(item):
    return item.did == 9001

def condition02(item):
    return len(item.name) == 2

def find_all(condition):
    for item in list_employees:
        # if len(item.name) == 2:
        # if condition02(item):
        # if condition01(item):
        if condition(item):
            yield item

for item in find_all(condition01):
    print(item)

for item in  IterableHelper.find_all(list_employees,condition01):
    print(item)
