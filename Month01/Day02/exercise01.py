'''
练习1：古代的秤，一斤十六两。在终端中获取两，计算几斤零几两。

效果：
    请输入总两数：100
    结果为：6斤4两
'''
# 1 获取数据
total_liang = int(input('请输入总两数:'))

# 2 数据计算
jin = total_liang // 16
liang = total_liang % 16

# 3 显示数据
print(jin, '斤' + str(liang) + '两')
