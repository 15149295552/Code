"""
      yield -> 生成器函数
"""
"""
class MyRange:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        number = 0
        while number < self.end:
            yield number
            number += 1

# for number in MyRange(5):
#     print(number)# 0 1 2 3 4
obj = MyRange(5)
iterator = obj.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)  # 0 1 2 3 4
    except StopIteration:
        break
"""


def my_range(end):
    number = 0
    while number < end:
        yield number
        number += 1


for item in my_range(5):
    print(item)

# obj = my_range(5)
# iterator = obj.__iter__()
# while True:
#     try:ss
#         item = iterator.__next__()
#         print(item)  # 0 1 2 3 4
#     except StopIteration:
#         break

# 生成器伪代码
"""
class generator: # 生成器 = 可迭代对象 + 迭代器
    def __iter__(self): # 可迭代对象
        return self 
    
    def __next__(self): # 迭代器
        计算数据
        return 数据 
"""
