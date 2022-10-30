"""
    练习：创建颜色类，数据包含r、g、b、a，实现颜色对象累加。
"""


class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __imul__(self, other):
        self.r *= other.r
        self.g *= other.g
        self.b *= other.b
        self.a *= other.a
        return self

c01 = Color(50, 0, 0, 200)
c02 = Color(0, 100, 0, 100)
c01 *= c02  # c01.__imul__(c02)
print(c01.__dict__)
# print( c01 *= c02 )
