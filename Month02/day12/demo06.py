"""
    重写
        __str__  为了呈现
        --repr-- 为了拷贝
        __add__  为了相加(根据类型决定行为)
        __iadd__ 为了累加(+=在自身基础上改变,+创建新数据)
        __eq__ 决定对象相同
        __gt__ 决定对象大小
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "x分量是:%s,y分量是:%s" % (self.x, self.y)

    def __gt__(self, other):
        return self.x > other.x

list01 = [
    Vector2(1, 1),
    Vector2(3, 3),
    Vector2(2, 2),
    Vector2(6, 6),
    Vector2(4, 4),
    Vector2(5, 5),
]
print(max(list01)) # 内部:自动执行__gt__

# 修改列表内部元素
# list01.sort() # 升序
list01.sort(reverse=True) #  降序
# 返回新列表,不改变旧列表
# new = sorted(list01)
new = sorted(list01,reverse=True)
print(new)
print(list01)
