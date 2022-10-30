# 练习：
#     创建子类：狗(跑)，鸟类(飞)
#     创建父类：动物(吃)
#     体会子类复用父类方法
#     体会 isinstance 与 type 的作用.

class Animal:
    def eat(self):
        print('eat')

class Dog(Animal):
    def run(self):
        print('run')

class Bird(Animal):
    def fly(self):
        print('fly')

# 子类Dog/Bird 继承 父类 Animal --> 继承了父类的方法eat
a01 = Animal()
d01 = Dog()
b01 = Bird()

# d01.run()
# d01.eat()
#
# b01.fly()
# b01.eat()

# isinstance 与 type 函数
# 狗对象 是一种 动物类
print(isinstance(d01, Animal))
# 鸟对象 是一种 动物类
print(isinstance(b01, Animal))

# 狗类 是 动物类
print(type(d01) == Animal)