# 商品字典
dict_commodity_infos = {
    1001: {"name": "屠龙刀", "price": 10000},
    1002: {"name": "倚天剑", "price": 10000},
    1003: {"name": "金箍棒", "price": 52100},
    1004: {"name": "口罩", "price": 20},
    1005: {"name": "酒精", "price": 30},
}

# 订单列表
list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]

# 1.打印所有商品信息,
# ​   格式：商品编号xx, 商品名称xx, 商品单价xx.
def print_commodity():
    '''
        打印商品信息
    :return: None
    '''
    for code, commodity in dict_commodity_infos.items():
        print(f'商品编号:{code}, 商品名称:{commodity["name"]}, 商品单价:{commodity["price"]}')

# print_commodity()

# 2.打印所有订单中的信息,
# 格式：商品编号xx, 购买数量xx.
def print_order():
    '''
        打印订单信息
    :return: None
    '''
    for order in list_orders:
        print(f'商品编号:{order["cid"]}, 购买数量:{order["count"]}')

# print_order()

# 3. 打印所有订单中的商品信息,
# 格式：商品名称xx, 商品单价: xx, 数量xx.
def print_order_commodity():
    '''
        打印所有订单中的商品信息
    :return: None
    '''
    for order in list_orders:
        code = order['cid']
        commodity = dict_commodity_infos[code]
        print(f'商品名称:{commodity["name"]}, 商品单价: {commodity["price"]}, 数量:{order["count"]}')

# print_order_commodity()

# 4.查找数量最多的订单(使用自定义算法, 不使用内置函数)
# 假设法
def find_max_order():
    '''
        查找数量最多的订单
    :return: None
    '''
    max_order = list_orders[0]
    for i in range(1, len(list_orders)):
        if max_order['count'] < list_orders[i]['count']:
            max_order = list_orders[i]
    return max_order

# print(find_max_order())


# 5.根据购买数量对订单列表降序(大 --> 小)排列
# 冒泡排序
def order_count_desc():
    '''
        根据购买数量对订单列表降序
    :return: None
    '''
    for i in range(len(list_orders)-1):
        for j in range(i+1, len(list_orders)):
            if list_orders[i]['count'] < list_orders[j]['count']:
                list_orders[i], list_orders[j] = list_orders[j], list_orders[i]

order_count_desc()
print(list_orders)
