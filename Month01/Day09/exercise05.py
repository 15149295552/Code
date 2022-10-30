# 练习：创建对象计数器，统计[构造方法]执行的次数

class Counter:
    # 类变量
    times = 0

    def __init__(self, name):
        self.name = name
        # self.times = times

    @classmethod
    def calculate_times(cls):
        cls.times += 1
        print('被调用的次数:', cls.times)

    # def complate_times(self):   # 实例方法
    #     self.times += 1
    #     print('被调用的次数:', self.times)

c01 = Counter('x')
Counter.calculate_times()
c02 = Counter('y')
Counter.calculate_times()
c03 = Counter('y')
Counter.calculate_times()

# c01 = Counter('x', 1)
# c01.complate_times()
# c01.complate_times()
# c02 = Counter('x', 1)
# c02.complate_times()
# c02.complate_times()