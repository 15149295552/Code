'''
面试：不能使用for循环实现对容器中元素获取并打印。
    练习1：创建列表，使用迭代思想，打印每个元素.
    练习2：创建字典，使用迭代思想，打印每个键值对.
'''

# list_data = [1, 2, 3, 4]
#
# # 1 调用__iter__方法返回迭代器
# iterator = list_data.__iter__()
#
# # 2 通过__next__方法获取下一个数据对象
# while True:
#     try:
#         item = iterator.__next__()
#         print(item)
#     # 3 当迭代器中无数据,则触发 StopIteration 异常
#     except StopIteration:
#         break


dict_data = {'name': '德德', 'age': 29}

# 1 调用__iter__方法返回迭代器
iterator = dict_data.__iter__()

# 2 通过__next__方法获取下一个数据对象
while True:
    try:
        item = iterator.__next__()
        print(item, dict_data[item])
    # 3 当迭代器中无数据,则触发 StopIteration 异常
    except StopIteration:
        break
