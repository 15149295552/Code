"""
    练习：创建颜色类，数据包含r、g、b、a，实现颜色对象相加。
"""


class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        return str(self.__dict__)

    def __sub__(self, other):
        if type(other) == Color:  # 传入不同类型,执行不同操作
            r = self.r - other.r
            g = self.g - other.g
            b = self.b - other.b
            a = self.a - other.a
        else:
            r = self.r - other
            g = self.g - other
            b = self.b - other
            a = self.a - other
        return Color(r, g, b, a)


c01 = Color(50, 0, 0, 200)
c02 = Color(0, 100, 0, 100)
c03 = c01 - c02  # c01.__sub__(c02)
c04 = c01 - 10  # c01.__sub__(10)
print(c03)
