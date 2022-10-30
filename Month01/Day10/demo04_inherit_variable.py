# 继承  -  数据(变量)

class Animals:
    def __init__(self, name):
        self.name = name

class Dog(Animals):
    def __init__(self, age, name):
        super().__init__(name)   # 调用父类构造方法,会将子类对象传入,从而为子类对象添加name属性
        # Animal.__init__(self, name)   # 不推荐
        self.age = age

# 1 当子类无构造方法时,则会调用父类的构造方法,所以在子类实例化时需要传递对应的参数
# d01 = Dog('拉布拉多')
# print(d01.__dict__)

# 2 当子类中有构造方法时,则会优先调用自身的构造方法,若想要继承父类构造方法中定义的属性,则需要使用 super() --> 父类, 调用父类的构造方法
d02 = Dog(1, '拉布拉多')
print(d02.__dict__)

