"""
-- 在商品列表，获取所有名称与单价

-- 在商品列表中，获取所有单价小于10000的商品

-- 对商品列表，根据单价进行降序排列

-- 获取元组中长度最大的列表  ([1,1],[2,2,2],[3,3,3])
"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price


list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]
res1 = list(map(lambda item: (item.name, item.price), list_commodity_infos))
print(res1)
res2 = list(filter(lambda item: item.price < 10000, list_commodity_infos))
print(res2)
list_commodity_infos.sort(key=lambda c: c.price, reverse=True)
print(list_commodity_infos)
tupel_data = ([1, 1], [2, 2, 2], [3, 3, 3])
print(max(tupel_data, key=lambda item: len(item)))