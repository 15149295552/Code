# 闭包

# 1 必须是内嵌函数
# def func01(x):   # 外部函数
#     def func02():  # 内嵌函数
#         # 2 内嵌函数中必须使用外部函数中的变量
#         y = 10
#         print(y - x)
#
#     # func02()
#     # 3 外部函数必须返回内嵌函数
#     return func02
#
# # 按照函数内存执行: 函数调用结束后,栈帧被释放(存在栈帧中的变量被释放)
# # 闭包: 因内嵌函数中需要使用到外部函数的变量,因此外部函数中的变量不释放
# f = func01(10)    # f = func02
# f()   # func02()


# 闭包的应用1: 使用逻辑连续
# 1 必须是内嵌函数
def myMoney():
    my_money = 1000
    def cost(name, price):
        ''' 花钱 '''
        # 2 在内嵌函数中使用了外部函数的变量
        nonlocal my_money
        my_money -= price
        print(f'买 {name}, 花了 {price},剩余: {my_money}' )

    # 3 外部函数必须返回内嵌函数
    return cost

spend = myMoney()    # spend = cost
spend('奥特曼', 200)
spend('遥控车', 100)
spend('小飞机', 300)

