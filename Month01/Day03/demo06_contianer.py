# 容器类型
# str  (重点)
# list  (重点)
# dict  (重点)
# tuple
# set

# 运算符
# str
a = 'hello'
b = 'world'

# 拼接： +  (重点)
# print(a + b)
# print(a, b)

# 拼接后赋值： +=
# a += b    # a = a + b
# print(a, b)


# 重复： *
# print(a * 5)
# print(a * 5.3)

# 重复后赋值： *=
# a *= 3
# print(a)

# print('-' * 50)


# 比较: 比较同位置的字符串的 Unicode 编码值
# print('Python' > 'python')
# print(ord('P'), ord('p'))    # ord 返回字符的Unicode值
# print(ord('鑫'), chr(37995))  # chr 返回Unicode值对应的字符


# 拼接重要性
# path = 'C:/oumasoft_sac/yy'
# file1 = 'python.txt'
# file2 = 'java.txt'
# print(path + '/' + file1)
# print(path + '/' + file2)
#
# '''
# https://bj.lianjia.com/ershoufang/pg2/
# https://bj.lianjia.com/ershoufang/pg3/
# https://bj.lianjia.com/ershoufang/pg4/
# https://bj.lianjia.com/ershoufang/pg9/
# '''
#
# base_path = 'https://bj.lianjia.com/ershoufang/pg'
# for i in range(1, 11):
#     print(base_path + str(i) + '/')


# 成员运算符（重点）
# string = 'Welcome to Beijing'
#
# print('welcome' in string)   # False 区分大小写
# print('ot' not in string)  # True 字符串是有序
# print('Bei' in string)  # True 子字符串


# 索引: str[index]
#      B    e    i    j    i     n    g
# 正向  0    1    2    3    4     5    6
# 反向  -7   -6   -5   -4   -3    -2   -1

string = 'Beijing'

# ’就近原则‘：从那个方向数方便，从那个方向开始
print('j', string[3], string[-4])
print('B', string[0], string[-7])
print('g', string[6], string[-1])

# 注意：
# print(string[8])     # IndexError: 索引值越界

# 函数：len(string)   --> 返回字符串的长度
print('长度：', len(string))
print('B', string[-len(string)])
print('g', string[len(string)-1])

# 切片



