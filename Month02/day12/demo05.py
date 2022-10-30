"""
    重写
        __str__  为了呈现
        --repr-- 为了拷贝
        __add__  为了相加(根据类型决定行为)
        __iadd__ 为了累加(+=在自身基础上改变,+创建新数据)
        __eq__
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x分量是:%s,y分量是:%s" % (self.x, self.y)

    def __eq__(self, other):
        # return self.x == other.x
        # return self.x == other.x and self.y == other.y
        return self.__dict__ == other.__dict__


pos01 = Vector2(1, 1)
pos02 = Vector2(1, 1)

# 比较地址:判断__eq__函数,默认比较地址,重写可比较内容
print(pos01 == pos02)  # 内部：pos01.__eq__(pos02)
# 身份运算符:比较地址
print(pos01 is pos02)  # id(pos01) == id(pos02)

list01 = [
    Vector2(1, 1),
    Vector2(3, 3),
    Vector2(2, 2),
    Vector2(6, 6),
    Vector2(4, 4),
    Vector2(5, 5),
]
print(Vector2(2, 2) in list01)
print(list01.count(Vector2(1, 1)))
list01.remove(Vector2(4, 4))
