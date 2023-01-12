"""

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

# (1)在汽车列表中查找所有汽车的品牌brand
print(IterableHelper.select(list_car, lambda item: item.brand))
# (2)在汽车列表中查找第一个中型车rank
res2 = IterableHelper.first(list_car, lambda car: car.rank == "中型车")
print(res2.__dict__)
# (3)在汽车列表中查找最后一中型车rank
res3 = IterableHelper.last(list_car, lambda car: car.rank == "中型车")
print(res3.__dict__)
# (4)在汽车列表中查找所有价格小于100000的汽车price
res4 = IterableHelper.find_all(list_car, lambda element: element.price < 100000)
print(res4)  # 加入断点
# for item in res4:
#     print(item.__dict__)
# (5)在汽车列表中查找最贵的汽车price
res5 = IterableHelper.get_max(list_car, lambda c: c.price)
print(res5.__dict__)
# (6)累加所有汽车的价格
print(IterableHelper.sum(list_car, lambda c: c.price))

# (1)在电影列表中查找所有演员姓名actor
print(IterableHelper.select(list_movie, lambda m: m.actor))
# (2)在电影列表中查找所有搞笑的电影type
res8 = IterableHelper.find_all(list_movie, lambda element: element.type == "搞笑")
print(res8)  # 加入断点
# (3)在电影列表中查找万里归途name
res9 = IterableHelper.first(list_movie, lambda car: car.name == "万里归途")
print(res9.__dict__)
# (4)删除所有战争类型的电影type
print(IterableHelper.delete_all(list_movie, lambda element: element.type == "战争"))
# (5)在电影列表中查找最后一个搞笑的电影
res11 = IterableHelper.last(list_movie, lambda car: car.type == "搞笑")
print(res11.__dict__)
