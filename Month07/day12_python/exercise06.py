"""
    实现下列功能：
       在汽车列表中查找所有"中型车"
       在汽车列表中查找所有价格小于180000的汽车
       在汽车列表中查找"迈腾"
       在汽车列表中查找第一个"中型车"
"""
from common.iterable_tools import IterableHelper


class Car:
    def __init__(self, brand="", price=0, rank=""):
        self.brand = brand
        self.price = price
        self.rank = rank

def condition01(item):
    return item.rank == "中型车"

def condition02(item):
    return item.price < 180000

def condition03(item):
    return item.brand == "迈腾"

# 与condition01相同
# def condition04(item):
#     return item.rank == "中型车"

list_car = [
    Car("五菱宏光", 46000, "微面"),
    Car("迈腾", 19000, "中型车"),
    Car("雅阁", 170000, "中型车"),
]

list_re = IterableHelper.find_all(list_car,condition01)
for item in list_re:
    print(item.__dict__)

list_re = IterableHelper.find_all(list_car,condition02)
for item in list_re:
    print(item.__dict__)

re = IterableHelper.first(list_car,condition03)
print(re.__dict__)

re = IterableHelper.first(list_car,condition01)
print(re.__dict__)
