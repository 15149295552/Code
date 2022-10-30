"""
    创建汽车类，实例化两个对象并调用其函数，画出内存图。

    数据：品牌、车牌、颜色、油量

    行为：启动(油量减少2)，加速(油量减少5)
"""


class Car: # 所有单词首字母大写,多个单词不用下划线隔开
    def __init__(self, color, oil, brand="", license=""):
        self.color = color
        self.brand = brand
        self.license = license
        self.oil = oil

    def start(self):
        print("启动")
        self.oil -= 2

    def speed_up(self):
        print("加速")
        self.oil -= 5

ben_chi = Car("白色", 50, "奔驰", "京C007")
bi_ya_di = Car("黑色", 50)
ben_chi.start() # -2
ben_chi.speed_up() # -5

print(ben_chi.__dict__)
print(bi_ya_di.__dict__)
