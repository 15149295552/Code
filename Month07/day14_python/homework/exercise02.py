"""
3. 需求：
        定义函数，在电影列表中删除阿凡达2
        定义函数，在汽车列表中删除雅阁
    步骤：
        -- 根据需求，写出函数。
        -- 因为主体逻辑相同,核心算法不同.
           所以使用函数式编程思想(分、隔、做)
           创建通用函数delete_single
            -- 在当前模块中调用

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

"""
def delete_single01():
    for i in range(len(list_movie)):
        if list_movie[i].name == "阿凡达2":
            del list_movie[i]
            return True
    return False

def delete_single02():
    for i in range(len(list_car)):
        if list_car[i].brand == "雅阁":
            del list_car[i]
            return True
    return False

print(delete_single01())

def condition01(item):
    return item.name == "阿凡达2"

def condition02(item):
    return item.brand == "雅阁"

def delete_single(iterable,condition):
    for i in range(len(iterable)):
        # if list_movie[i].name == "阿凡达2":
        # if condition01(iterable[i]):
        # if condition02(iterable[i]):
        if condition(iterable[i]):
            del iterable[i]
            return True
    return False


print(delete_single(list_movie, condition01))
print(delete_single(list_movie, lambda m: m.type == "战争"))
"""

print(IterableHelper.delete_single(list_movie, lambda m: m.type == "战争"))