# 内置高阶函数

# map(function, iterable)

# 需要: 将一下列表中所有的元素的平方存储起来
# list01 = [2, 5, 7, 9, 3]

# object01 = map(lambda x: x ** 2, list01)  '基于函数计算新的可迭代对象'
# print(object01)
# for item in object01:
#     print(item)


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

# for item in map(lambda emp: emp.name, list_employees):
#     print(item)
#
# date = '2022/8/19'
# print(list(map(int, date.split('/'))))
# year, month, day = map(int, date.split('/'))
# print(year, month, day, type(year))


# filter(function, iterable)   '过滤'
# list01 = [2, 5, 7, 9, 3]
#
# object2 = filter(lambda x: x > 5, list01)
# print(object2)
#
# for item in object2:
#     print(item)


# sorted(iteable, *, key, reverse=False)   # 排序,返回排序后的结果
list01 = [-2, 5, -7, 9, -3]
# 方法1:
list01.sort(key=lambda x: x if x > 0 else -x, reverse=True)
print(list01)

# 方法2:
# list01 = [-2, 5, -7, 9, -3]
# list02 = sorted(list01, key=abs, reverse=True)
# print(list02, list01)
#
# tuple_employees = (
#     Employee(1001, 9002, "师父", 60000),
#     Employee(1002, 9001, "孙悟空", 50000),
#     Employee(1003, 9002, "猪八戒", 20000),
#     Employee(1004, 9001, "沙僧", 30000),
#     Employee(1005, 9001, "小白龙", 15000),
# )
#
# result = sorted(tuple_employees, key=lambda emp: emp.money, reverse=True)
# for temp in result:
#     print(temp)


# max(iterable, key=function)   '最大值'
# min(iterable, key=function)   '最小值'

list01 = [-2, 5, -7, 9, -3]
print(max(list01, key=abs))
print(min(list01, key=abs))