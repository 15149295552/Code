class Commodity:
    # 构造方法: 实例化时[自动]被调用
    def __init__(self, cid, name, price):
        self.cid = cid  # 实例变量: 实例对象.变量名
        self.name = name
        self.price = price

    # 实例方法: 实例对象.实例方法名()
    def print_single_commodity(self):
        print(f"编号:{self.cid},商品名称:{self.name},商品单价:{self.price}")


# 商品列表: 存储商品对象
list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]


class Order:
    def __init__(self, cid, count):
        self.cid = cid
        self.count = count


# 订单列表: 存储订单对象
list_orders = [
    Order(1001, 1),
    Order(1002, 3),
    Order(1005, 2)
]


# 1. 定义函数,打印所有商品信息,格式：商品编号xx,商品名称xx,商品单价xx.
def print_commodity_infos():
    for commodity in list_commodity_infos:  # commodity: 商品对象
        # 实例变量: 调用实例方法
        commodity.print_single_commodity()


# print_commodity_infos()

# 2. 定义函数,打印商品单价小于2万的商品信息
def print_price_in_2w():
    for commodity in list_commodity_infos:  # commodity: 商品对象
        if commodity.price < 20000:
            commodity.print_single_commodity()


print_price_in_2w()


# 3. 定义函数,打印所有订单中的商品信息,
def print_order_infos():
    for order in list_orders:  # order: 订单对象
        for commodity in list_commodity_infos:  # commodity: 商品对象
            if order.cid == commodity.cid:
                print(f"商品名称{commodity.name},"
                      f"商品单价:{commodity.price},"
                      f"数量{order.count}.")
                break  # 跳出内层循环


print_order_infos()


# 4. 查找最贵的商品(使用自定义算法,不使用内置函数)
def commodity_max_by_price():
    # 假设法
    max_value = list_commodity_infos[0]  # 第1商品对象
    for i in range(1, len(list_commodity_infos)):
        if max_value.price < list_commodity_infos[i].price:
            max_value = list_commodity_infos[i]
    return max_value


# max_price_commodity_object = commodity_max_by_price()
# print(max_price_commodity_object)   # 直接打印对象,查看的是对象在内存中的存储地址
# print(max_price_commodity_object.print_single_commodity())

# 5. 根据单价对商品列表降序排列
def descending_order_by_price():
    for r in range(len(list_commodity_infos) - 1):
        for c in range(r + 1, len(list_commodity_infos)):
            if list_commodity_infos[r].price < list_commodity_infos[c].price:
                list_commodity_infos[r], list_commodity_infos[c] = list_commodity_infos[c], list_commodity_infos[r]


descending_order_by_price()
for commodity in list_commodity_infos:
    commodity.print_single_commodity()
