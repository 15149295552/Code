# 继承  -  方法

class Animal:
    def eat(self):
        print('吃')

class Person(Animal):   # 自类Person继承父类Animal
    def say(self):
        print('hello')

class Pig(Animal):   # 自类Pig继承父类Animal
    def sleep(self):
        print('睡了')

p01 = Person()
p01.say()
p01.eat()    # 子类如果没有此方法,则会调用父类的方法

p02 = Pig()
p02.sleep()
p02.eat()

p01.sleep()   # '兄弟类'中的方法不能被调用