"""
    重写
        __str__  为了呈现
        --repr-- 为了拷贝
        ...
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x分量是:%s,y分量是:%s"%(self.x,self.y)

    def __add__(self, other):
        # 重点：需要根据传入的类型,决定操作的行为
        if type(other) == Vector2:
            x = self.x + other.x
            y = self.y + other.y
        else:
            x = self.x + other
            y = self.y + other
        return Vector2(x, y)

pos01 = Vector2(1, 2)
pos02 = Vector2(5, 6)
pos03 = pos01 + pos02  # 内部： pos01.__add__(pos02)
pos04 = pos01 + 6 # 内部： pos01.__add__(6)
print(pos03)