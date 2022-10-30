# 练习：创建颜色类，数据包含r、g、b、a，实现颜色对象相加。
# 练习：创建颜色类，数据包含r、g、b、a，实现颜色对象累加。
# 练习：创建颜色列表，实现in、count、index、max、sort运算。

class Color:
    def __init__(self, r, g, b, a):
        self.r = r
        self.g = g
        self.b = b
        self.a = a

    def __str__(self):
        return f'{self.r}-{self.g}-{self.b}-{self.a}'

    def __add__(self, other):  # +
        return Color(self.r + other.r,
                     self.g + other.g,
                     self.b + other.b,
                     self.a + other.a)

    def __iadd__(self, other):  # +=
        self.r += other.r
        self.g += other.g
        self.b += other.b
        self.a += other.a
        return self

    def __eq__(self, other):  # ==
        return self.r == other.r and \
               self.g == other.g and \
               self.b == other.b and \
               self.a == other.a

    def __gt__(self, other):  # >
        return self.r > other.r and \
               self.g > other.g and \
               self.b > other.b and \
               self.a > other.a

c01 = Color(1, 2, 3, 4)
c02 = Color(5, 0, 1, 4)
print(c01 + c02)  # 调用 __add__方法
c01 += c02  # 调用 __iadd__方法
print(c01)

list_color = [
    Color(1, 2, 3, 4),
    Color(2, 2, 3, 4),
    Color(3, 2, 3, 4),
    Color(4, 2, 3, 4)
]

# 实现in、count、index、max、sort运算
print(Color(3, 2, 3, 4) in list_color)  # 调用 __eq__方法
print(list_color.count(Color(3, 2, 3, 4)))  # 调用 __eq__方法
print(list_color.index(Color(3, 2, 3, 4)))  # 调用 __eq__方法

print(max(list_color))    # 调用 __gt__方法
print(list_color.sort())   # 调用 __gt__方法
