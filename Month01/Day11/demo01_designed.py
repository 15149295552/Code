# 程序设计
"""
    手雷爆炸,伤害玩家(扣血,碎屏)和敌人(扣血,头顶爆字)。
    变化点：鸭子,房子...
    写出体现三大特征的代码：
        封装：根据需求[分解]出手雷类,玩家类,敌人类
        继承：使用攻击目标[隔离]手雷与玩家,敌人
        多态：手雷[调用]攻击目标,在玩家和敌人对象中体现了不同效果
              玩家和敌人分别重写了攻击目标的受伤方法
"""

class Grenade:
    def __init__(self, atk):
        self.atk = atk

    def explode(self, obj):
        # if type(obj) == Player:   # 可扩展性差
        #     obj.demage(self.atk)
        # elif type(obj) == Enemy:
        #     obj.death(self.atk)
        if isinstance(obj, AttackTarget):    # 不变
            obj.demage(self.atk)

class AttackTarget:   # 1 抽象为一个父类
    def demage(self, value):  # 2 统一行为
        pass

class Player(AttackTarget):
    def __init__(self, hp):
        self.hp = hp

    def demage(self, value):  # 3 重写
        self.hp -= value
        print('剩余血量:', self.hp)
        print('碎屏')

class Enemy(AttackTarget):
    def __init__(self, hp):
        self.hp = hp

    def demage(self, value):
        self.hp -= value
        print("剩余血量:", self.hp)
        print('头顶爆字')

class House(AttackTarget):
    def demage(self, value):
        print('爆炸了')

g01 = Grenade(50)
p01 = Player(200)
e01 = Enemy(300)
h01 = House()

g01.explode(p01)
g01.explode(e01)
g01.explode(h01)