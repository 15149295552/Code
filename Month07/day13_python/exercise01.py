"""
    可参照：大于DAY12/exercise06
    1. 实现下列功能：
        在汽车列表中查找所有"中型车"
        在汽车列表中查找所有价格小于180000的汽车
        在汽车列表中查找"迈腾"
        在汽车列表中查找第一个"中型车"

    可参照：大于DAY13/homework/exercise01
    2. 实现下列功能：
        在电影列表中查找阿凡达2的电影对象
        在电影列表中查找所有搞笑的电影
        在电影列表中查找所有沈腾的电影
        在电影列表中查找张译的第一个电影
"""
from common.iterable_tools import IterableHelper


class Car:
    def __init__(self, brand="", price=0, rank=""):
        self.brand = brand
        self.price = price
        self.rank = rank


class Movie:
    def __init__(self, name="", type="", actor=""):
        self.name = name
        self.type = type
        self.actor = actor


list_car = [
    Car("五菱宏光", 46000, "微面"),
    Car("迈腾", 19000, "中型车"),
    Car("雅阁", 170000, "中型车"),
]

list_movie = [
    Movie("独行月球", "搞笑", "沈腾"),
    Movie("阿凡达2", "冒险", "萨姆·沃辛顿"),
    Movie("万里归途", "战争", "张译"),
    Movie("疯狂72小时", "搞笑", "闫妮"),
]
# def condition01(item):
#     return item.rank == "中型车"
#
# list_re = IterableHelper.find_all(list_car,condition01)

list_re = IterableHelper.find_all(list_car, lambda item: item.rank == "中型车")
for item in list_re:
    print(item.__dict__)

res2 = IterableHelper.find_all(list_car, lambda car: car.price < 180000)
print(res2)  # 建议加断点测试

res3 = IterableHelper.first(list_car, lambda c: c.brand == "迈腾")
print(res3.__dict__)

res4 = IterableHelper.first(list_car, lambda c: c.rank == "中型车")
print(res4.__dict__)
# ---------------
res5 = IterableHelper.first(list_movie,lambda m:m.name == "阿凡达2")
print(res5)

res6 = IterableHelper.find_all(list_movie, lambda item: item.type == "搞笑")
print(res6)

res7 = IterableHelper.find_all(list_movie, lambda item: item.actor == "沈腾")
print(res7)

res8 = IterableHelper.first(list_movie,lambda m:m.actor == "张译")
print(res8.__dict__)
