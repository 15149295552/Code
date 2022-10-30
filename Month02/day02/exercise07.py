"""
    练习：在终端中输入商品单价、购买的数量和支付金额。
         计算应该找回多少钱。
    效果：
    请输入商品单价：5
    请输入购买数量：3
    请输入支付金额：20
    应找回：5.0
"""
# 1. 获取数据
price = float(input("请输入商品单价："))
count = float(input("请输入购买数量："))
money = float(input("请输入支付金额："))
# 2. 逻辑计算
result = money - price * count
# 3. 显示结果
# print("应找回：result")
print("应找回：" + str(result))
