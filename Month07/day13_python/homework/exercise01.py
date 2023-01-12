"""
    (1) 在电影列表中查找阿凡达2的电影对象
    (2) 在电影列表中查找所有搞笑的电影
    (3) 在电影列表中查找所有沈腾的电影
    (4) 在电影列表中查找张译的第一个电影
"""
from common.iterable_tools import IterableHelper


class Movie:
    def __init__(self, name="", type="", actor=""):
        self.name = name
        self.type = type
        self.actor = actor

list_movie = [
    Movie("独行月球", "搞笑", "沈腾"),
    Movie("阿凡达2", "冒险", "萨姆·沃辛顿"),
    Movie("万里归途", "战争", "张译"),
    Movie("疯狂72小时", "搞笑", "闫妮"),
]

def condition01(item):
    return item.name == "阿凡达2"

def condition02(m):
    return m.type == "搞笑"

def condition03(m):
    return m.actor == "沈腾"

def condition04(item):
    return item.actor == "张译"

res01 = IterableHelper.first(list_movie,condition01)
print(res01.__dict__)

res02 = IterableHelper.find_all(list_movie,condition02)
for item in res02:
    print(item.__dict__)

res03 = IterableHelper.find_all(list_movie,condition03)
for item in res03:
    print(item.__dict__)

res04 = IterableHelper.first(list_movie,condition04)
print(res04.__dict__)