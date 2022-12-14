"""
    字面值(各种写法)
"""
# 1.整型int字面值
# 十进制DEC:每位使用10种状态计数，0~9，逢10进1
number01 = 20
# 二进制BIN:每位使用2种状态计数，0~1，逢2进1
# 0 1 10 11 100  101  110 ...
number02 = 0b10
# 八进制OCT:每位使用8种状态计数，0~7，逢8进1
# 0 1 2 ... 7  10  11  12 ...
number03 = 0o20
# 十六进制HEX:每位使用16种状态计数，0~9 a~f，逢16进1
# 0 1 ~ 9 a b ~ f 10 11 12 ...
number04 = 0x20

# 2. 浮点型字面值
# 小数
number05 = 1.2
# 科学计数法
number06 = 12e-1
print(number05 == number06) # True
number07 =0.000000000000000000000000000000000001
print(number07) # 1e-36