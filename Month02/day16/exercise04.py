"""
    需求2：delete_all
    定义函数，删除部门是9002的所有员工
    定义函数，删除薪资大于20000的所有员工
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
# 正序删除多个,会造成漏删
# del list_employees[0],list_employees[1]
# 所以删除多个元素应该倒序
# del list_employees[1], list_employees[0]
def delete_all01():
    # 4 3 2 1 0
    count = 0
    for i in range(len(list_employees)-1,-1,-1):
        if list_employees[i].money > 20000:
            del list_employees[i]
            count += 1
    return count

def delete_all02():
    count = 0
    for i in range(len(list_employees)-1,-1,-1):
        if list_employees[i].did == 9002:
            del list_employees[i]
            count += 1
    return count


print(delete_all01())


def delete_all(condition):
    count = 0
    for i in range(len(list_employees)-1,-1,-1):
        # if list_employees[i].did == 9002:
        if condition(list_employees[i]):
            del list_employees[i]
            count += 1
    return count


print(delete_all(lambda e: e.did == 9002))
"""
print(IterableHelper.delete_all(list_employees, lambda e: e.did == 9002))
