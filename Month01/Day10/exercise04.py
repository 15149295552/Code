# 练习：
#     创建父类：车(品牌，速度)
#     创建子类：电动车（electrocar）(电池容量（capacity）)
#     创建子类对象(具有3个实例属性)

class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Electrocar(Car, object):
    def __init__(self, brand, speed, capacity):
        super().__init__(brand, speed)
        self.capacity = capacity

e01 = Electrocar("爱玛", 60, 10000)
print(e01.__dict__)