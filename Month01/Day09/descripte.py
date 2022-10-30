class Bank:
    total_money = 10000000   # 类变量: 所有对象同有的数据 ('饮水机')  --> '大家的'

    def __init__(self, name=None, money=None):
        self.name = name     # 实例变量: 单个对象的数据 ('水杯') --> '自己的'
        self.money = money    

    def print_bank_info(self):  # 实例方法: 单个对象的功能或行为 --> '自己的喝水的行为'
        print(f'{self.name} 有 {self.money} 元')

    @classmethod     # 类方法: 用来表达所有对象共同的功能或行为 --> '每个人喝水的行为'
    def use_total_money(cls, money):
        cls.total_money -= money    # 修改类变量
        print('总行的钱剩余:', cls.total_money)  # 访问类变量

b01 = Bank('亦庄支行', 2000000)
Bank.use_total_money(b01.money)   # 调用类方法