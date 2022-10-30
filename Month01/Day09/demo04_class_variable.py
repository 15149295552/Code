# 类成员 - 类变量

# 实例:银行-支行的关系

class Bank:
    ''' 表达银行类 '''
    # 类变量: 所有实例对象所共享的数据 ('大家的')
    total_money = 10000000

    def __init__(self, name=None, money=None):
        # 实例变量(实例属性)
        self.name = name
        self.money = money


# Bank('亦庄支行', 2000000)  --> 实例化
# b01: 实例化对象
b01 = Bank('亦庄支行', 2000000)

# 访问类变量
print(b01.total_money)
print(b01.__dict__)
print(Bank.total_money)  # 推荐

# 修改类变量的值
b01.total_money = 200000  # 为实例对象添加属性(实例对象无法修改类变量的值)
# print(b01.total_money)
# print(b01.__dict__)
Bank.total_money = 200000  # 推荐
print(Bank.total_money)
