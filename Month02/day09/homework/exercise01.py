list_commodity_infos = [
    {"cid": 1001, "name": "屠龙刀", "price": 10000},
    {"cid": 1002, "name": "倚天剑", "price": 10000},
    {"cid": 1003, "name": "金箍棒", "price": 52100},
    {"cid": 1004, "name": "口罩", "price": 20},
    {"cid": 1005, "name": "酒精", "price": 30},
]


# 1. 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_commodity_infos():
    for commodity in list_commodity_infos:
        print(f"编号:{commodity['cid']},商品名称:{commodity['name']},商品单价:{commodity['price']}")


# 2. 获取单价大于500的商品名称与单价
def get_names_by_price():
    """

    :return: list类型..
    """
    list_data = []
    for item in list_commodity_infos:
        if item["price"] > 500:
            list_data.append((item["name"], item["price"]))
    return list_data


# 3. 查找最贵的商品(使用自定义算法,不使用内置函数)
def get_max_by_price():
    """

    :return: 字典类型,最贵的商品
    """
    max_value = list_commodity_infos[0]
    for i in range(1, len(list_commodity_infos)):
        if max_value["price"] < list_commodity_infos[i]["price"]:
            max_value = list_commodity_infos[i]
    return max_value


# 4. 根据单价对商品列表降序排列
def descending_order_by_price():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r]["price"] < list_commodity_infos[c]["price"]:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]


# -------------------------
descending_order_by_price()
print_commodity_infos()
# value = get_max_by_price()
# print(value)
print(get_names_by_price())
