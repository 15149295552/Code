# A）由数字、字母、下划线组成

# B）不能以数字开头

# C）严格区分大小写

# D）不能使用Python关键字【深蓝色加粗】
# import keyword
# print(keyword.kwlist)

# E）不能使用Python内置函数名
# print = 11
# a = 10
# print(a)


# 赋值
# 内存：变量name存储了“帅哥” 的存储存储地址
# name = '帅哥'
# print(name)

# 注意：变量在使用前一定要赋值
# print(age)

# a = b = 10
# print(a, b)

# 数据交换
# a = 10
# b = 20
# a, b = b, a
# print(a, b)

a = b = 20
b = 30
print(a)

# 删除
# 手动
# del b   # 解除了变量与数据之间的关联关系
# print(b)