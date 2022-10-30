# 封装 - 私有化
# 包含:
#  实例成员
#  类成员

# 定义wife类,定义2个属性:name/age
# class Wife:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# w01 = Wife('双儿', 16)
# print(w01.name, w01.age)
#
# w01.age = 200
# print(w01.name, w01.age)

# 问题:
#   1 对象的属性不能在类外被随意修改
#   2 数据不能超过有效范围


# class Wife:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age   # 私有化
#
#
# w01 = Wife('双儿', 16)
# print(w01.name, w01.__age)   # 在类外不能直接被访问
# print(w01.__dict__)
#
# w01.__age = 200                # 为实例对象添加属性(私有化实例变量在类外不能直接被修改)
# print(w01.name, w01.__age)
# print(w01.__dict__)

# print(w01._Wife__age)    # 屏蔽: _类名__属性名
# w01._Wife__age = 18      # 不推荐
# print(w01._Wife__age)    # 不推荐
# print(w01.__dict__)

# 问题: 屏蔽: _类名__属性名 方式修改或访问不推荐使用,而直接在类外不能访问或修改,若要实现在类外访问或修改?
# 措施: 提供2个方法:访问/修改(保护实例变量) + 数据有效性验证

# class Wife:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age   # 私有化
#
#     def get_age(self):    # 访问(读取)
#         return self.__age    # 在类内可以访问私有实例变量
#
#     def set_age(self, value):  # 修改(写入)
#         # 数据有效性验证
#         if 0 <= value < 60:
#             self.__age = value   # 在类内可以修改私有实例变量
#         else:
#             print("年龄值错误")
#
# w01 = Wife('双儿', 16)
# print(w01.__dict__)
#
# # 访问
# print(w01.get_age())
#
# # 修改
# w01.set_age(200)
# print(w01.get_age())
# print(w01.__dict__)
#
#
# w02 = Wife('双儿', 116)
# print('W02:', w02.__dict__)

# 问题: 在对象实例化时,也需要做数据有效性验证, self.__age 调用 set_age 方法

# class Wife:
#     def __init__(self, name, age):
#         self.name = name
#         # self.__age = self.set_age(age)   # 私有化
#         # self.set_age(age)    # 不太符合面向对象的语法
#         self.age = age
#
#     def get_age(self):    # 访问(读取)
#         return self.__age    # 在类内可以访问私有实例变量
#
#     def set_age(self, value):  # 修改(写入)
#         # 数据有效性验证
#         if 0 <= value < 60:
#             self.__age = value   # 在类内可以修改私有实例变量
#         else:
#             print("年龄值错误")
#
#     # 访问/修改实例变量: 调用set_age/get_age 方法
#     age = property(get_age, set_age)
#
# w01 = Wife('双儿', 16)
# print(w01.__dict__)
#
# # 访问
# print(w01.age)

# 终极写法: 遵循面向对象的语法 + 保护实例变量 + 数据有效性验证
# 可读可写模式
# class Wife:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     @property
#     def age(self):    # 访问(读取)
#         return self.__age    # 在类内可以访问私有实例变量
#
#     @age.setter
#     def age(self, value):  # 修改(写入)
#         if 0 <= value < 60:  # 数据有效性验证
#             self.__age = value   # 在类内可以修改私有实例变量
#         else:
#             print("年龄值错误")
#
# w01 = Wife('双儿', 16)
# print(w01.__dict__)
#
# # 访问
# print(w01.age)
#
# # 修改
# w01.age = 20
# print(w01.age)



# # 只读模式
# class Wife:
#     def __init__(self, name, age):
#         self.name = name
#         self.__age = age
#
#     @property
#     def age(self):    # 访问(读取)
#         return self.__age    # 在类内可以访问私有实例变量
#
# w01 = Wife('双儿', 16)
# print(w01.__dict__)
#
# # 访问
# print(w01.age)
#
# # 修改
# w01.age = 20     # AttributeError: can't set attribute
# print(w01.age)


# 只写模式
# class Wife:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def set_age(self, value):  # 修改(写入)
#         if 0 <= value < 60:  # 数据有效性验证
#             self.__age = value   # 在类内可以修改私有实例变量
#         else:
#             print("年龄值错误")
#
#     age = property(None, set_age)
#
# w01 = Wife('双儿', 16)
# print(w01.__dict__)

# 访问
# print(w01.age)   # AttributeError: unreadable attribute

# 修改
# w01.age = 20
# # print(w01.age)
# print(w01.__dict__)


# 私有化 - 实例方法
class Animal:
    def __init__(self, name=None, age=None):
        self.name = name
        self.__age = age

    def __modify_age(self):   # 私有化实例方法
        self.__age += 1
        print('当前年龄为:', self.__age)

    def main(self):
        self.__modify_age()

a01 = Animal('咻米', 1)
# a01.__modify_age()    # 私有化实例方法在类外不能直接调用
# a01._Animal__modify_age()   # 屏蔽 --> 不推荐
a01.main()



