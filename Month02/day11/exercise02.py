"""
    父类：车(品牌，速度)
    创建子类：电动车(电池容量,充电功率)
"""


# 构造函数:创建对象的方式

class Car:
    def __init__(self, brand, speed):  # 4
        self.brand = brand
        self.speed = speed


class ElectricCar(Car):
    # 1. 子类构造函数参数：父类参数+子类参数
    def __init__(self, brand, speed, battery_capacity, charging_power):  # 2
        # 2. 通过super调用父类构造函数
        super().__init__(brand, speed)  # 3
        self.battery_capacity = battery_capacity
        self.charging_power = charging_power


bc = Car("奔驰", 220)
print(bc.__dict__)

wl = ElectricCar("蔚来", 180, 10000, 220)  # 1
print(wl.__dict__)
