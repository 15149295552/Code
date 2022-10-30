"""
    面向过程 --> 面向对象
"""
class Employee:
    def __init__(self,eid,did,name,money):
        self.eid = eid
        self.did = did
        self.name = name
        self.money = money

list_employees = [
    Employee(1001,9002,"师父",60000),
    Employee(1002,9001,"孙悟空",50000),
    Employee(1003,9002,"猪八戒",20000),
    Employee(1004,9001,"沙僧",30000),
    Employee(1005,9001,"小白龙",15000),
]
# 1. 打印所有员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元。
def print_employees():
    for emp in list_employees:
        print(f"{emp.name}的员工编号是{emp.eid},部门编号是{emp.did},月薪{emp.money}元.")


# 2. 查找部门时9002的员工名称
def get_name_by_did_9002():
    """
        ...
    :return: 列表类型,所有姓名
    """
    list_name = []
    for emp in list_employees:
        if emp.did == 9002:
            list_name.append(emp.name)
    return list_name


# 3. 定义函数,获取薪资最低的员工
def get_min_by_money():
    min_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if min_value.money > list_employees[i].money:
            min_value = list_employees[i]
    return min_value


# 4. 定义函数，根据购买数量对订单列表降序(大->小)排列
def descending_order_by_money():
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            if list_employees[r].money < list_employees[c].money:
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]


descending_order_by_money()
print(list_employees)

value = get_min_by_money()
print(value.__dict__)

print(get_name_by_did_9002())

print_employees()
