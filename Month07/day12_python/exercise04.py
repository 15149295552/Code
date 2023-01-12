"""
    实现下列功能：
       在汽车列表中查找所有"中型车"
       在汽车列表中查找所有价格小于180000的汽车
       在汽车列表中查找"迈腾"
       在汽车列表中查找第一个"中型车"
"""
class Car:
    def __init__(self, brand="", price=0, rank=""):
        self.brand = brand
        self.price = price
        self.rank = rank

list_car = [
    Car("五菱宏光", 46000, "微面"),
    Car("迈腾", 19000, "中型车"),
    Car("雅阁", 170000, "中型车"),
]
