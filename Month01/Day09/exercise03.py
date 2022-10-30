# 练习1：以面向对象思想,描述下列情景.
# 玩家攻击敌人，敌人受伤（根据玩家攻击力，减少敌人的血量）

'''
分析:
    玩家类:
        数据(属性):攻击力
        方法(功能):攻击
    敌人类:
        数据(属性):血量
        方法(功能):受伤
'''
class Player:
    def __init__(self, atk):
        self.atk = atk
        # 方法2: 每次都是攻击都是同一个敌人
        # self.enemy = Enemy(100)

    def attack(self, enemy):
        ''' 玩家攻击敌人(敌人对象)  '''
        # 方法1: 每次都是攻击的新敌人
        # e01 = Enemy(100)   # 实例化敌人对象 (每次创建一个新的敌人对象)
        # e01.demage(self.atk)
        # self.enemy.demage(self.atk)

        # 方法3:
        enemy.demage(self.atk)

class Enemy:
    def __init__(self, hp):
        self.hp = hp

    def demage(self, atk):
        self.hp -= atk    # 根据玩家攻击力，减少敌人的血量
        print('敌人剩余血量:', self.hp)

p01 = Player(20)
e01 = Enemy(100)
e02 = Enemy(100)
p01.attack(e01)
p01.attack(e01)
p01.attack(e01)
p01.attack(e02)
p01.attack(e02)


