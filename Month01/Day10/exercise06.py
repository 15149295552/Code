# 练习：
#   直接打印商品对象: xx的编号是xx,单价是xx
#   直接打印敌人对象: xx的攻击力是xx,血量是xx

class Commodity(object):
    def __init__(self, cid=0, name="", price=0):
        self.cid = cid
        self.name = name
        self.price = price

    def __str__(self):   # 重写父类object类中的__str__方法
        return f'{self.name}的编号是:{self.cid},单价是:{self.price}'

class Enemy:
    def __init__(self, name="", atk=0, hp=0):
        self.name = name
        self.atk = atk
        self.hp = hp

    def __str__(self):
        return f'{self.name}的攻击力是:{self.atk},血量是:{self.hp}'

c01 = Commodity(1, '毛巾', 8)
print(c01)
e01 = Enemy('灭霸', 100, 1000)
print(e01)
