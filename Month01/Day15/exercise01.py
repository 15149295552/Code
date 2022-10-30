# 练习：使用闭包模拟以下情景：
#     在银行开户存入10000
#      购买xx商品花了xx元
#      购买xx商品花了xx元


def bank(money):
    # money: 外部函数嵌套作用域中的变量(形参属于局部变量)
    def cost(name, price):
        nonlocal money   # 声明money为外部函数嵌套作用域
        money -= price   # 修改外部函数嵌套作用域中的变量
        print(f'购买{name}商品花了{price}元,剩余的钱数:{money}')

    return cost

spend = bank(1000)
spend('手机壳', 60)
spend('机械键盘', 230)
