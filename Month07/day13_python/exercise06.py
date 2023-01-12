"""
    练习:
        定义函数，在员工列表中查找薪资最小的员工
        定义函数，在员工列表中查找编号最小的员工
    步骤：
        -- 根据需求，写出函数。
        -- 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数get_min
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

# def get_min(condition):
#     min_value = list_employees[0]
#     for i in range(1, len(list_employees)):
#         # if min_value.money > list_employees[i].money:
#         if condition(min_value) > condition(list_employees[i]):
#             min_value = list_employees[i]

res1 = IterableHelper.get_min(list_employees,lambda item:item.money)
res2 = IterableHelper.get_min(list_employees,lambda item:item.eid)
print(res1.__dict__)