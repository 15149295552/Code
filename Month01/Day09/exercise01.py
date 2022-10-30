'''
练习1：创建狗类，实例化两个对象并调用其方法。
​	数据：品种、昵称、身长、体重
​	行为：吃(体重增长1)
'''

class Dog:
    def __init__(self, kind, nickname, height, weight):
        # 定义实例变量: 表达实例对象的特征
        self.kind = kind
        self.name = nickname
        self.height = height
        self.weight = weight

    def eat(self, food):  # 实例方法: 表达实例对象的功能或行为
        self.weight += 1
        print(f'{self.name} 的体重是:{self.weight},吃的是:{food}')

# 实例化对象: gou
gou = Dog('拉布拉多', '旺财', 1, 20)

# 调用实例方法
gou.eat('骨头')