"""
    练习：
        直接打印商品对象: xx的编号是xx,单价是xx
        直接打印敌人对象: xx的攻击力是xx,血量是xx
"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):  # 必须返回字符串
        return f"{self.name}的编号是{self.cid},单价是{self.price}"


class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp

    def __str__(self):
        return "%s的攻击力是%d,血量是%d" % (self.name, self.atk, self.hp)


c01 = Commodity(1001, "屠龙刀", 10000)
print(c01)

e01 = Enemy("灭霸")
print(e01)  # 内部：e01.__str__()
