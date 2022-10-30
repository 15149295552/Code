# '''
#     运算符
# '''
#
# # 算术运算符
# print(3 + 3)
# print(13 - 3)
# print(13 * 3)
# print(13 / 3)
# print(13.8 / 3)
# print(12 / 3)    # python3 中 / 结果是浮点数
# print(13 % 5)    # 取余
#
# print(2 ** 10)   # 求幂
# print(2 ** 128)
# print(12 // 5)   # 取整数商
#\
# # 西瓜13元/个，100元买几个，剩余几个？
# print('个数:', 100 // 13)
# print('剩余:', 100 % 13)
#
# # 数字：234，分别获取各个位上的数
# print('百位：', 234 // 100)
# print('十位：', 234 // 10 % 10)
# print('十位：', 234 % 100 // 10)
# print('个位：', 234 % 10)

# 增强运算符
# 适用性：累计运算
# 作用：在原来计算的基础上，将结果重新赋值给变量（不用创建更多的变量）--节省内存空间
# 今年16岁
# age = 16
#
# # 两年后
# age = age + 2
# print(age)
#
# # 相当于上面的写法
# age += 2
# print(age)
#
# age -= 2
# age **= 2
# print(age)
#
# # ++   --  python无此运算 --》使用增强运算符替代


# 比较运算符
# 返回值：bool类型，结果是：True/False
# 适用性：命题判断
# print(4 > 3)
# print(4 >= 4)   # 4 > 4 或者 4 == 4
# print(4 < 3)
# print(4 <= 3)
# print(4 == 3)   # 等于，区分：= 赋值
# print(4 != 3)   # 不等于
#
# # 特殊用法
# # 判断一个数是否在某个区间内：0 <= age <= 18
# age = 10
# print(0 <= age <= 18)   # 链式比较



# 逻辑运算符
# 适用性：逻辑关系判断
# and  -- 并且（一假俱假）
# house = input('请输入是否有房：')
# money = int(input('请输入存款金额：'))
# print(house == '有' and money >= 100000)

# or -- 或者（一真俱真）
# house = input('请输入是否有房：')
# money = int(input('请输入存款金额：'))
# print(house == '有' or money >= 100000)

# not -- 不/非（真亦假，假亦真）
# money = int(input('请输入存款金额：'))
# print(not money < 10000)

# 短路逻辑
# print(float(input("请输入身高（m）:")) > 1.8 and int(input("请输入资产:")) >= 1000000)
# print(float(input("请输入身高（m）:")) > 1.8 or int(input("请输入资产:")) >= 1000000)


# 身份运算符
# a = 1000
# b = 1000
# print(a is b)
# print(id(a))
# print(id(b))
#
# a = -10
# b = -10
# print(a is b)
# print(id(a))
# print(id(b))

# == 与 is/is not 有什么区别？
# == 比较的是数值是否相等
# is/is not 比较的是数值所占用计算机内存地址是否相等
# python解释器一般都是采用cpython，使用小整数池（常用字母、数值是[-5, 256]这些数据固定在计算机的内存中，这些都是常用的数据，为了减少系统频繁的开辟或销毁内存空间，占用资源）
