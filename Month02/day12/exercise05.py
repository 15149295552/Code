"""
    练习：创建颜色列表，实现in、count、index、max、sort运算。
"""


class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __eq__(self, other):
        # return id(self) == id(other)
        return self.__dict__ == other.__dict__

    def __gt__(self, other):
        return self.r > other.r
        # 如果有多个排序的条件,继续学习第三门课
        # return self.g > other.g
        # return self.b > other.b
        # return self.a > other.a


list01 = [
    Color(10, 10, 10, 10),
    Color(30, 30, 30, 30),
    Color(20, 20, 20, 20),
]
# Color(10, 10, 10, 10) == Color(20, 20, 20, 20)
# Color(30, 30, 30, 30) == Color(20, 20, 20, 20)
# Color(20, 20, 20, 20) == Color(20, 20, 20, 20)
list01.remove(Color(20, 20, 20, 20))

list01.sort()
print(list01)
