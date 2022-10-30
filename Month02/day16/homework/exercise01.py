"""
2. 使用IterableHelper完成下列功能
    -- 在商品列表中查找名称是倚天剑的商品
    -- 在商品列表中查找编号是1003的商品
    -- 在商品列表中查找所有价格大于等于10000的商品
    -- 在商品列表中查找编号小于1003的商品数量

"""
from common.iterable_tools import IterableHelper

class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):
        return str(self.__dict__)

list_commodity_infos = [
    Commodity(1001, "屠龙刀", 10000),
    Commodity(1002, "倚天剑", 10000),
    Commodity(1003, "金箍棒", 52100),
    Commodity(1004, "口罩", 20),
    Commodity(1005, "酒精", 30),
]
# for item in list_commodity_infos:
#     if item.name == "倚天剑":
#         print(item)

print(IterableHelper.find_single(list_commodity_infos,lambda c:c.name == "倚天剑"))
print(IterableHelper.find_single(list_commodity_infos,lambda c:c.cid == 1003))
for item in IterableHelper.find_all(list_commodity_infos,lambda c:c.price > 10000):
    print(item)
print(IterableHelper.get_count(list_commodity_infos, lambda item: item.cid > 1003))

