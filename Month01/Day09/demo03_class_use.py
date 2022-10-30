# 跨类调用

# 需求: 老张开车去东北
# 分析: 人类/车类 --> 人要开车去哪里

# 语义: 每去一个地方都需要创建一个新的车对象 [浪费资源]
# class Human:
#     def __init__(self, name):
#         self.name = name
#
#     def go_to(self, where):
#         car = Car()  # 创建了车对象 ('买了一辆车')
#         print(self.name, '去', where)
#         car.run()  # 调用车行驶的方法('车载着人去哪儿')
#
#
# class Car:
#     def run(self):
#         print('载着..')
#
#
# lz = Human('老张')
# lz.go_to('东北')
# lz.go_to('北京')


# 语义:每次去一个新的地方都使用的同一个车对象 [人与车绑定] --> 不灵活
# class Human:
#     def __init__(self, name):
#         self.name = name
#         self.car = Car()  # 创建了车对象 ('买了一辆车')
#
#     def go_to(self, where):
#         print(self.name, '去', where)
#         self.car.run()  # 调用车行驶的方法('车载着人去哪儿')
#
# class Car:
#     def run(self):
#         print('载着..')
#
#
# lz = Human('老张')
# lz.go_to('东北')
# lz.go_to('北京')



# 语义: 每去一个地方,可以选择交通工具 --> 灵活 (transpost 用来接收交通工具对象)
class Human:
    def __init__(self, name):
        self.name = name

    def go_to(self, where, transpost):
        print(self.name, '去', where)
        transpost.run()  # 调用交通工具对象的行驶的方法

class Car:
    def run(self):
        print('载着..')

class Plane:
    def run(self):
        print('飞着..')

lz = Human('老张')
car = Car()
plane = Plane()
lz.go_to('东北', car)
lz.go_to('北京', plane)