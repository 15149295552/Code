'''
练习2：分红包，在终端输入红包金额、红包个数，打印每人平均可以分得的金额。
效果：
    请输入红包金额：10
    请输入红包个数：5
    打印：每人平均可以分得的金额：2 元
'''

money = input('请输入红包金额：')
count = input('请输入红包个数：')

result = float(money) / int(count)

print('每人分得金额：' + str(result) + '元')