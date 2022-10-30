"""
    练习2：古代的秤，一斤十六两。
    在终端中获取两，计算几斤零几两。
    效果：
    请输入总两数：100
    结果为：6斤4两
"""
total_liang = int(input("请输入总两数：")) # 100
jin = total_liang // 16 # 6
liang = total_liang % 16 # 4
print("结果为：" + str(jin) + "斤" + str(liang) + "两")

