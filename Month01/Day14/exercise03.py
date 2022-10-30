class Employee:
    def __init__(self, eid, did, name, money):
        self.eid = eid  # 员工编号
        self.did = did  # 部门编号
        self.name = name
        self.money = money

    def __str__(self):
        return f'{self.eid}-{self.did}-{self.name}-{self.money}'


list_employees = [
    Employee(1001, 9002, "师父", 60000),
    Employee(1002, 9001, "孙悟空", 50000),
    Employee(1003, 9002, "猪八戒", 20000),
    Employee(1004, 9001, "沙僧", 30000),
    Employee(1005, 9001, "小白龙", 15000),
]

from common.iterableHelper import IterableHelper


# 需求1：定义函数，在员工列表中查找编号是1003的员工
# 需求2：定义函数，在员工列表中查找姓名是孙悟空的员工
def condition01(emp, value):
    return emp.eid == value


# lambda emp, value: emp.eid == value

def condition02(emp, value):
    return emp.name == value


# lambda emp, value: emp.name == value

# def find(condition, value):
#     for emp in list_employees:
#         # if emp.eid == 1003:
#         # if emp.name == '孙悟空':
#         if condition(emp, value):
#             return emp

# print(IterableHelper.find(list_employees,
#                           condition01,
#                           1005))
print(IterableHelper.find(list_employees,
                          lambda emp, value: emp.eid == value,
                          1005))

# print(IterableHelper.find(list_employees, condition02, '孙悟空'))
print(IterableHelper.find(list_employees,
                          lambda emp, value: emp.name == value,
                          '孙悟空'))

for item in filter(lambda emp: emp.name == '孙悟空', list_employees):
    print(item)

# 需求3: 定义函数，在员工列表中统计薪资大于20000的员工数量
# 需求4: 定义函数，在员工列表中统计名字超过2个字的员工数量
def condition03(emp, value):
    return emp.money > value


def condition04(emp, value):
    return len(emp.name) > value


# def count(condition, value):
#     number = 0
#     for emp in list_employees:
#         # if emp.money > 20000:
#         # if len(emp.name) > 2:
#         if condition(emp, value):
#             number += 1
#     return number

# print(IterableHelper.count(list_employees, condition03, 20000))
# print(IterableHelper.count(list_employees, condition04, 2))

print(IterableHelper.count(list_employees,
                           lambda emp, value: emp.money > value,
                           20000))
print(IterableHelper.count(list_employees,
                           lambda emp, value: len(emp.name) > value,
                           2))


# 需求5: 定义函数，在员工列表中薪资最高的员工对象
# 需求6: 定义函数，在员工列表中名字字数最长的员工对象
def condition05(employee):
    return employee.money


def condition06(employee):
    return len(employee.name)


# def max(condition):
#     # 假设法
#     max_employee = list_employees[0]
#     for i in range(1, len(list_employees)):
#         if condition(list_employees[i]) > condition(max_employee):
#             max_employee = list_employees[i]
#         # if condition(list_employees[i]) > condition(max_employee):
#         # if len(list_employees[i].name) > len(max_employee.name):
#         #     max_employee = list_employees[i]
#     return max_employee

# print(IterableHelper.max(list_employees, condition05))
# print(IterableHelper.max(list_employees, condition06))

print(IterableHelper.max(list_employees,
                         lambda employee: employee.money))
print(IterableHelper.max(list_employees,
                         lambda employee: len(employee.name)))

print(max(list_employees, key=lambda employee: employee.money))
print(min(list_employees, key=lambda employee: employee.money))