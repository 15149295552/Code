"""
    内置高阶函数
"""


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

# map 映射
# 结果 = list(map(函数,可迭代对象))
# 所有员工的编号
print(list(map(lambda e: e.eid, list_employees)))

# filter 过滤器
# 结果 = list(filter(函数,可迭代对象))
res2 = list(filter(lambda item: item.did == 9001, list_employees))
for item in res2:
    print(item.__dict__)

# max 最大/最小
# 结果 = max(可迭代对象,key = 函数)
# 结果 = min(可迭代对象,key = 函数)
res3 = max(list_employees, key=lambda item: item.money)
print(res3.__dict__)

# sort 排序
# 可迭代对象.sort(key = 函数) # 升序排列
# 可迭代对象.sort(key = 函数,reverse=True) # 降序排序
list_employees.sort(key=lambda e: e.did)
list_employees.sort(key=lambda e: e.did, reverse=True)
print(list_employees)
