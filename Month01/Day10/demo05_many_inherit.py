# 多继承

# 多继承 - 方法
# class A:
#     def display(self):
#         print('A')
#
# class B:
#     pass
#     # def display(self):
#     #     print('B')
#
# class C(A):
#     def display(self):
#         print('C')
#
# class D(C):
#     def display(self):
#         print('D')
#
# class E(B, D):
#     pass
#     # def display(self):
#     #     print('E')
#
# e01 = E()
# e01.display()
#
# # 查看子类的继承列表(继承链)
# print(E.mro())


# 多继承 - 数据
class Animal:
    def __init__(self, name):
        self.name = name

class Dog:
    def __init__(self, color):
        self.color = color

class Kt(Animal, Dog):
    def __init__(self, age, name, color):
        super().__init__(name)   # 父类: Animal
        Dog.__init__(self, color)  # 父类: Dog
        self.age = age

k01 = Kt(2, 'ki', '金色')
print(k01.__dict__)











