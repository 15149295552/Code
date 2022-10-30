# 多态 - polymorphic

# 父类动物的叫, 子类狗/猫的叫

class Animal:
    def cry(self):
        print('叫')

class Dog(Animal):
    def cry(self):    # 重写: 子类同名的方法会覆盖父类的方法
        print('旺旺')

class Cat(Animal):
    def cry(self):    # 重写目的: 父类的行为不满足子类的需求时
        super().cry()  # 调用父类的cry方法
        print('喵喵')

d01 = Dog()
c01 = Cat()
d01.cry()   # 调用时,会调用子类的方法
c01.cry()



