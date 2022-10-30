# 外部函数嵌套作用域的变量使用

# 场景: 收红包

# my_money = 1000

def myMoney():
    ''' 这是我的钱 '''
    my_money = 1000

    def cost(name, price):
        ''' 花钱 '''
        nonlocal my_money
        # my_money -= 200
        # print('买 奥特曼, 花了200,剩余:', my_money)

        my_money -= price
        print(f'买 {name}, 花了 {price},剩余: {my_money}' )

    cost('奥特曼', 200)
    cost('小汽车', 500)

myMoney()

# my_money -= 300
# print(my_money)