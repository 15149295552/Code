"""
    print(666 == "666") # 整数666等于字符串666
    print(27 % 10 == 2) # 27的个位是2
    print(float(input("请输入你的身高：")) > 170) # 你的身高大于170
"""
print(666 == "666")  # False
print(27 % 10 == 2)  # False

# 输入的是正数
# print(float(input("请输入数字：")) > 0)
# 输入的是星期
# print(1 <= int(input("请输入星期：")) <= 7)
# 输入的不是偶数（是奇数）
print(int(input("请输入整数：")) % 2 != 0)
