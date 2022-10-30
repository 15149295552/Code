"""
    创建子类：狗(跑)，鸟类(飞)
    创建父类：动物(吃)
    体会子类复用父类方法
    体会 isinstance 、issubclass 与 type 的作用.
"""


class Animal:
    def eat(self):
        print("吃")


class Dog(Animal):
    def run(self):
        self.eat()
        print("跑")


class Bird(Animal):
    def fly(self):
        print("飞")


a01 = Animal()
d01 = Dog()
b01 = Bird()

a01.eat()
# 子类复用父类
d01.run()
d01.eat()

# 类型 与 类型 是一种关系
print(issubclass(Animal, Dog))
# 对象 与 类型 是一种关系
print(isinstance(b01, Animal))
# 动物对象 与 动物类型 相同
print(type(a01) == Animal)  # True
