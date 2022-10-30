# 运算符重载

# 需求: 实现坐标的相关操作
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'x={self.x}, y={self.y}'

    def __add__(self, other):    # +
        # 不可变/可变 --> 新的对象
        return Location(self.x+other.x, self.y+other.y)

    def __pow__(self, power):   # **
        return self.x ** power + self.y ** power

    def __iadd__(self, other):  # +=
        self.x += other.x
        self.y += other.y
        return self

    def __gt__(self, other):   # >
        return self.x > other.x and self.y > other.y

    def __eq__(self, other):   # ==
        return self.x == other.x and self.y == other.y

# 实例化坐标对象
loc01 = Location(3, 1)
loc02 = Location(2, 0)

# 实现坐标对象的相加运算
# print(loc01 + loc02)   # 默认调用 __add__ 方法
# print(loc01 ** 2)   # 默认调用 __pow__ 方法
print(id(loc01))

loc01 += loc02   # 默认调用 __iadd__ 方法 loc01 = loc01 + loc02
print(loc01, id(loc01))

print(loc01 > loc02)   # 默认调用 __gt__ 方法


list_loc = [
    Location(1, 3),
    Location(2, 5),
    Location(1, 3),
    Location(3, 2),
    Location(4, 1),
]

print(Location(1, 3) in list_loc)
print(list_loc.index(Location(1, 3)))
print(list_loc.count(Location(1, 3)))

# lists = [1, 3]
# # print(lists + [2, 4])
# print(id(lists))
# lists += [2, 4]
# print(id(lists))