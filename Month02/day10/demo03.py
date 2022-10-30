"""
    跨类调用
        根据行为划分类
        根据数据划分对象
"""
"""
def func02():
    func01()

def func01():
    pass

func02()
"""

# 请以面向对象思想,描述下列情景
#   老张开车去东北
#   老李开车去东北
#   老孙开车去东北
#   驾驶  行驶

# 语法1:直接创建对象
# 语义1:老张每次去东北开新车
"""
class Person:
    def __init__(self, name=""):
        self.name = name

    def drive(self,position):
        print("去",position)
        car = Car()
        car.run()

class Car:
    def run(self):
        print("行驶")

lz = Person("老张")
ll = Person("老李")
lz.drive("东北")
"""

# 语法2:在构造函数中创建对象
# 语义2:老张每次去东北开自己的车
"""
class Person:
    def __init__(self, name=""):
        self.name = name
        self.car = Car()

    def drive(self,position):
        print("去",position)
        self.car.run()

class Car:
    def run(self):
        print("行驶")

lz = Person("老张")
lz.drive("东北")
"""


# 语法3:通过参数传入对象
# 语义3:老张每次去东北通过交通工具
class Person:
    def __init__(self, name=""):
        self.name = name

    def drive(self, position, vehicle):
        print("去", position)
        vehicle.run()


class Car:
    def run(self):
        print("行驶")


lz = Person("老张")
car = Car()
lz.drive("东北", car)
