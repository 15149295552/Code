"""
    使用lambda完成下列功能
        在员工列表中查找所有部门是9002的员工数量
        在员工列表中查找所有员工编号大于1002的员工工数量
        在员工列表中查找所有部门是9001的员工
        在员工列表中查找所有姓名是2个字的员工
        在员工列表中查找编号是1003的员工
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

print(IterableHelper.get_count(list_employees,lambda item:item.did == 9002))
print(IterableHelper.get_count(list_employees,lambda item:item.eid  > 1002))
for item in IterableHelper.find_all(list_employees,lambda e:e.did == 9001):
    print(item)
for item in IterableHelper.find_all(list_employees,lambda e:len(e.name) == 2):
    print(item)
print(IterableHelper.find_single(list_employees, lambda element: element.eid == 1003))