# 数据类型

# int --> 整数
# print(4, -4, type(-4), type(0))
# print('二进制表示方式：', 0b011)
# print('八进制表示方式：', 0o011)
# print('十六进制表示方式：', 0x011)

# float --> 小数
# print(type(-3.14), type(0.0))
# print(3e3)   # 3乘以10的3次方

# str --> 文本数据
# print(type('123'))
# print(type("a123"))

# bool --> 结果真假
# print(True, type(True))
# print(False, type(False))
# print(3 > 2)

# None --> 空（特殊不存在的对象）
# print(None, type(None))
# a = None
# a = 20
# a = None


# 类型转换
# str --> int
# float --> int
# a = '123'
# b = int(a)
# print(b, type(b))
# print(int(3.999))    # 去除小数部分

# str --> float
# print(float('3.445'))

# int --> str
# float --> str
# 适用性：结果拼接显示
# print('结果是:' + str(5))
# print('结果是:' + str(5.2))

# 使用场景：
float(input('请输入您的身高（m）：'))
int(input('请输入您的年龄：'))