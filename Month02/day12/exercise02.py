"""
    练习：
        自定义对象浅拷贝
            repr
            eval
"""


class Commodity:
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __repr__(self):
        return 'Commodity(%s, "%s", %s)'%(self.cid,self.name,self.price)


class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp

    def __repr__(self):
        return 'Enemy("%s", %s, %s)'%(self.name,self.atk,self.hp)

c01 = Commodity(1001, "屠龙刀", 10000)
c02 = eval(c01.__repr__())
c01.name = "刀刀"
print(c02.name)

e01 = Enemy("灭霸")
e02 = eval(repr(e01)) # 内部：e01.__repr__()
e01.name = "霸霸"
print(e02.name)

print(e01)