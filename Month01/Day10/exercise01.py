# 练习1：创建敌人类，并保护数据在有效范围内
#  数据：姓名、攻击力（0-100）、血量（0-500）
'''
    保护数据: 攻击力/血量
    实现模式: 可读可写模式
'''

class Enemy:
    def __init__(self, name, atk, hp):
        self.name = name
        self.atk = atk
        self.hp = hp

    # 读取方法(atk)
    @property
    def atk(self):
        return self.__atk

    # 写入方法(atk)
    @atk.setter
    def atk(self, value):
        if 0 <= value <= 100:
            self.__atk = value
        else:
            print('攻击力超出范围')

    # 读取方法(hp)   # 快捷写法:props --> 可读可写模式
    @property
    def hp(self):
        return self.__hp

    # 写入方法(hp)
    @hp.setter
    def hp(self, value):
        if 0 <= value < 500:
            self.__hp = value
        else:
            print('血量超过范围')


e01 = Enemy('灭霸', 99, 499)
print(e01.__dict__)
e02 = Enemy('灭霸2', 199, 499)
print(e02.__dict__)
e03 = Enemy('灭霸2', 99, 999)
print(e03.__dict__)
