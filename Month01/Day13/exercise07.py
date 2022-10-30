# # 练习1：定义函数,在列表中找出所有偶数
# list_data1 = [43, 43, 54, 56, 76, 87, 98]
#
# # 常规方法
# def find_even(lists):
#     '''
#         查找并返回偶数
#     :param lists: list,存储数据的列表
#     :return: list, 存储偶数的列表
#     '''
#     list_even = []
#     for item in lists:
#         if item % 2 == 0:
#             list_even.append(item)
#     return list_even
#
# list_result = find_even(list_data1)
# for item in list_result:
#     print(item)
#
# # 生成器函数
# def find_even1(lists):
#     '''
#         查找并返回偶数
#     :param lists: list,存储数据的列表
#     :return: list, 存储偶数的列表
#     '''
#     for item in lists:
#         if item % 2 == 0:
#             yield item
#
# for item in find_even1(list_data1):
#     print(item)


# 练习2：定义函数,在列表中找出所有数字
list_data2 = [43, "悟空", True, 56, "八戒", 87.5, 98]

# 常规方法
def find_number1(lists):
    list_number = []
    for data in lists:
        # if type(data) == int or type(data) == float or type(data) == bool:
        if type(data) != str:
            list_number.append(data)
    return list_number

list_result = find_number1(list_data2)
for item in list_result:
    print(item)

# 生成器函数实现
def find_number(lists):
    for data in lists:
        if type(data) != str:
            yield data

for item in find_number(list_data2):
    print(item)

'''
    结论: 
        若函数中返回单个数据,则推荐使用return语句 (return 数据)
        若函数中返回多个数据,则推荐使用yield语句 (yield 数据)
'''