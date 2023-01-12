"""
    实现下列功能：
       在员工列表中查找员工编号是1003的员工对象
       在员工列表中查找所有部门编号是9001的员工对象
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


# 参数：列表中的元素
# 返回值：True则返回该元素
def condition01(item):
    return item.eid == 1003


def condition02(e):
    return e.did == 9002

e1 = IterableHelper.first(list_employees, condition01)
print(e1.__dict__)

list_e = IterableHelper.find_all(list_employees, condition02)
for item in list_e:
    print(item.__dict__)
