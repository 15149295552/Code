"""
    内置高阶函数
"""


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
# 映射
# 获取所有员工姓名
for name in map(lambda item: item.name, list_employees):
    print(name)

# 过滤器
# 获取所有9001的员工
for emp in filter(lambda item: item.did == 9001, list_employees):
    print(emp)

# 获取最有钱的员工
print(max(list_employees, key=lambda item: item.money))

# 升序排列
# list_employees.sort(key = lambda e:e.did)
# 降序排列
list_employees.sort(key=lambda e: e.did, reverse=True)
print(list_employees)

# 不改变原列表,返回新列表
new = sorted(list_employees, key=lambda e: e.did)
new = sorted(list_employees, key=lambda e: e.did, reverse=True)
print(new)
