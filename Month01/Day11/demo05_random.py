# random  - 生成随机数
import random

# 生成随机浮点数
print(random.random())   # 范围:[0, 1)
print(random.uniform(2, 4))   # 范围:[a, b]

# 生成随机整数
print(random.randint(1, 10))  # 范围:[1,10]
print(random.randrange(1, 10, 2))  # 范围:(1,10,2)

# 从序列中随机返回元素#
L = [1, 2, 3, 6, 8, 9]
print(random.choice(L))     # 返回1个
print(random.sample(L, 3))     # 返回多个不重复的列表元素