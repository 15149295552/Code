# 迭代 iter

# 面试题: for的原理是什么?
# s = 'python'
#
# for char in s:
#     print(char)

# 1 调用__iter__方法返回迭代器
# 2 通过__next__方法获取下一个数据对象
# 3 当迭代器中无数据,则触发 StopIteration 异常

# s = 'python'
#
# # 1 调用__iter__方法返回迭代器
# iterator = s.__iter__()
# print(iterator, type(iterator))
#
# # 2 通过__next__方法获取下一个数据对象
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())
#
# # 3 当迭代器中无数据,则触发 StopIteration 异常
# print(iterator.__next__())


s = 'python'

# 1 调用__iter__方法返回迭代器
iterator = s.__iter__()
# print(iterator, type(iterator))

# 2 通过__next__方法获取下一个数据对象
while True:
    try:
        print(iterator.__next__())
    # 3 当迭代器中无数据,则触发 StopIteration 异常
    except StopIteration:
        break

