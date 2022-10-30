# ---------------全局变量(数据)-------------
list_employees = [
    {
        "eid": 1001,
        "did": 9002,
        "name": "师父",
        "money": 60000
    },
    {"eid": 1002, "did": 9001, "name": "孙悟空", "money": 50000},
    {"eid": 1003, "did": 9002, "name": "猪八戒", "money": 20000},
    {"eid": 1004, "did": 9001, "name": "沙僧", "money": 30000},
    {"eid": 1005, "did": 9001, "name": "小白龙", "money": 15000},
]

# ---------------定义函数(算法)-------------

# 1. 打印所有员工信息,
# 格式：xx的员工编号是xx,部门编号是xx,月薪xx元。
def print_employees():
    for emp in list_employees:
        print(f"{emp['name']}的员工编号是{emp['eid']},部门编号是{emp['did']},月薪{emp['money']}元.")


# 2. 查找部门时9002的员工名称
def get_name_by_did_9002():
    """
        ...
    :return: 列表类型,所有姓名
    """
    list_name = []
    for emp in list_employees:
        if emp["did"] == 9002:
            list_name.append(emp["name"])
    return list_name


# 3. 定义函数,获取薪资最低的员工
def get_min_by_money():
    min_value = list_employees[0]
    for i in range(1, len(list_employees)):
        if min_value["money"] > list_employees[i]["money"]:
            min_value = list_employees[i]
    return min_value


# 4. 定义函数，根据购买数量对订单列表降序(大->小)排列
def descending_order_by_money():
    for r in range(len(list_employees) - 1):
        for c in range(r + 1, len(list_employees)):
            if list_employees[r]["money"] < list_employees[c]["money"]:
                list_employees[r], list_employees[c] = list_employees[c], list_employees[r]


descending_order_by_money()
print(list_employees)

value = get_min_by_money()
print(value)

print(get_name_by_did_9002())

print_employees()
