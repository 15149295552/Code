"""
    创建图形管理器：
        1. 记录所有图形
        2. 计算总面积
    图形：
        1. 矩形
        2. 圆形
        ...
    要求：
        增加新图形,管理器代码不变.

分析:
    图形管理器类
        属性: list_graph
        方法: add_graph/calculate_area

    图形类:
        方法: area --> 统一行为/功能

    矩形类(图形类):
        属性: width/height
        方法: area

    圆形类(图形类):
        属性: raduis
        方法: area
"""
class GraphManager:
    def __init__(self):
        self.list_graph = []

    def add_graph(self, graph):
        self.list_graph.append(graph)

    def calculate_area(self):
        total_area = 0
        for graph in self.list_graph:
            total_area += graph.area()
        return total_area

class Graph:    # 1 抽象父类
    def area(self):   # 2 统一行为
        pass

class Rectangle(Graph):
    def __init__(self, width, height):
        self.w = width
        self.h = height

    def area(self):    # 3 重写
        # super().area()
        return self.w * self.h

class Round(Graph):
    def __init__(self, raduis):
        self.r = raduis

    def area(self):
        return 3.14 * self.r ** 2

gm = GraphManager()
rect = Rectangle(2, 3)
ro = Round(3)

gm.add_graph(rect)
gm.add_graph(ro)

print(gm.calculate_area())