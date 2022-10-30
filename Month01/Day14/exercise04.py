class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.cid}-{self.name}-{self.price}'


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]

# -- 在商品列表，获取所有名称与单价 map
commodity_result = map(lambda commodity: (commodity.name, commodity.price),
                       list_commodity_infos)

for commodity in commodity_result:
    print(commodity)

# -- 在商品列表中，获取所有单价小于10000的商品 filter
commodity_result2 = filter(lambda commodity: commodity.price < 10000,
                           list_commodity_infos)

for commodity in commodity_result2:
    print(commodity)

# -- 对商品列表，根据单价进行降序排列 sorted
commodity_result3 = sorted(list_commodity_infos,
                           key=lambda emp: emp.price,
                           reverse=True)

for commodity in commodity_result3:
    print(commodity)

# -- 获取元组中长度最大的列表  ([1,1],[2,2,2],[3,3,3])
tuple_data = ([1, 1], [2, 2, 2], [3, 3, 3])
print(max(tuple_data, key=len))



print(max(tuple_data, key=lambda x: x[0]))


list_orders = [
    {"cid": 1001, "count": 1},
    {"cid": 1002, "count": 3},
    {"cid": 1005, "count": 2},
]

print(max(list_orders, key=lambda x: x['count']))