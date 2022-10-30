"""
    重写
        __str__  为了呈现
        --repr-- 为了拷贝
        __add__
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x分量是:%s,y分量是:%s" % (self.x, self.y)

    # + 返回新对象
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2(x, y)

    # += 返回旧对象
    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

pos01 = Vector2(1, 2)
pos02 = Vector2(5, 6)
print(id(pos01))
pos01 += pos02
print(id(pos01))

# list01 = [1]
# list02 = [2]
# print(id(list01))
# list01 += list02
# print(id(list01))


# list01 = [1]
# list01 = list01 + [2]  # 算数运算符:创建新列表[1,2]
# list01 += [2]  # 增强运算符:在原有[1]基础上追加2
