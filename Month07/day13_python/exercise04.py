"""
    需求：
        定义函数，在员工列表中查找最后一个部门是9002的员工
        定义函数，在员工列表中查找最后一个薪资大于20000的员工
    步骤：
        -- 根据需求，写出函数。
        -- 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数last
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


# # 从头到尾读取
# for item in list_employees:
#     print(item.__dict__)

# 从尾到头读取(触发浅拷贝)
# for item in list_employees[  :  :-1]:
#     print(item.__dict__)

# 不包含结束值
# for i in range(len(list_employees) - 1, -1, -1):
#     # print(i) # 4 3 2 1 0
#     print(list_employees[i].__dict__)

"""
def last01():
    for i in range(len(list_employees) - 1, -1, -1):
        if list_employees[i].did == 9002:
            return list_employees[i]

def last02():
    for i in range(len(list_employees) - 1, -1, -1):
        if list_employees[i].money > 20000:
            return list_employees[i]

res1 = last02()
print(res1.__dict__)

def condition01(item):
    return item.did == 9002

def condition02(item):
    return item.money > 20000

# 委托、接口
def last(condition):
    for i in range(len(list_employees) - 1, -1, -1):
        # if list_employees[i].money > 20000:
        # if condition02(list_employees[i]):
        # if condition01(list_employees[i]):
        if condition(list_employees[i]):
            return list_employees[i]

res1 = last(condition01)
res2 = last(lambda a:len(a.name) == 2)
print(res2.__dict__)
"""

res1 = IterableHelper.last(list_employees,lambda item:item.did == 9001)
print(res1.__dict__)