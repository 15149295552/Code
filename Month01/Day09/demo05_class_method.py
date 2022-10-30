# 类成员 - 类方法

# 实例:每开一家支行,总行的钱减少

class Bank:
    total_money = 10000000

    def __init__(self, name=None, money=None):
        self.name = name
        self.money = money

        # 每开一家支行,总行的钱减少  --> 实例方法中可以访问/修改类变量
        # Bank.total_money -= self.money
        # Bank.use_total_money(self.money)   # 实例方法中可以调用类方法

    @classmethod     # 类方法: 用来表达所有对象共同的功能或行为 --> 操作类变量
    def use_total_money(cls, money):
        # cls: class, 类, 表示当前的类 --> Bank
        cls.total_money -= money    # 修改类变量
        print('总行的钱剩余:', cls.total_money)  # 访问类变量
        # print(self.name)

# 类变量存在优先于实例对象
b01 = Bank('亦庄支行', 2000000)
# print(Bank.total_money)
b01.use_total_money(b01.money)    # 不推荐
Bank.use_total_money(b01.money)   # 调用类方法

b02 = Bank('白水桥支行', 2000000)
# print(Bank.total_money)
Bank.use_total_money(b02.money)   # 调用类方法

b03 = Bank('立水桥支行', 5000000)
# print(Bank.total_money)
Bank.use_total_money(b03.money)   # 调用类方法