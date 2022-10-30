# 练习1： 定义函数, 在终端中打印一维列表.
# list01 = [5, 546, 6, 56, 76]
# for item in list01:
#     print(item)

# list02 = [7, 6, 879, 9, 909]
# for item in list02:
#     print(item)

# '定义功能'
def print_list(data):
    '''
        打印一维列表
    :param data: list,存储数据的列表
    :return: None
    '''
    for item in data:
        print(item)

# ‘使用功能’
list01 = [5, 546, 6, 56, 76]
list02 = [7, 6, 879, 9, 909]
print_list(list01)
print_list(list02)