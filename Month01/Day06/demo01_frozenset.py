# 固定集合 frozenset  (了解)

# 创建
s1 = frozenset()
print(s1, type(s1))

s2 = frozenset(range(5))
print(s2)

# 存在
s3 = frozenset({'java', 'c', 'python', 'php'})
print('c++' not in s3)

# 运算符
s4 = frozenset({0, 1, 2, 3, 4})
s5 = frozenset({1, 3, 4, 6, 7})
print('交集', s4 & s5)
print('并集', s4 | s5)
print('补集', s4 - s5)
print('对称集', s4 ^ s5)