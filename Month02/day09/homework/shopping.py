# 体现过程，隐藏实现。

# 数据
dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def shopping():
    """
        购物
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buying()
        elif item == "2":
            settlement()


def settlement():
    """
        结算
    """
    print_orders_info()
    total_price = calculate_total_price()
    paying(total_price)


def paying(total_price):
    """
        支付
    :param total_price: 需要支付的金额
    """
    while True:
        money = float(input("总价%d元，请输入金额：" % total_price))
        if money >= total_price:
            print("购买成功，找回：%d元。" % (money - total_price))
            list_order.clear()
            break
        else:
            print("金额不足.")


def calculate_total_price():
    """
        计算总价格
    :return: 总价格
    """
    total_price = 0
    for order in list_order:
        commodity = dict_commodity_info[order["cid"]]
        total_price += commodity["price"] * order["count"]
    return total_price


def print_orders_info():
    """
        打印所有订单信息
    """
    for item in list_order:
        commodity = dict_commodity_info[item["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], item["count"]))


def buying():
    """
        购买
    """
    print_commodity_info()
    order = create_order()
    list_order.append(order)
    print("添加到购物车。")


def input_commodity_id():
    """
        获取商品编号
    :return: int类型,商品编号
    """
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            return cid
        print("该商品不存在")


def create_order():
    """
        创建订单
    :return: 字典类型的订单
    """
    cid = input_commodity_id()
    count = int(input("请输入购买数量："))
    order = {"cid": cid, "count": count}
    return order


def print_commodity_info():
    """
        打印商品信息
    """
    for key, value in dict_commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


shopping()
