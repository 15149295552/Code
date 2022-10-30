'''
7、字符次数
    定义函数：输入一段字符串，存储字符及字符出现的次数，并打印出结果：字符：xx 出现的次数为：xx 次。

分析:
    列表方式: [字符1, 字符2, ...]   [次数1, 次数2, ...]
        1 定义函数: count_char_times(string)
        2 创建2个列表: list_chars  list_times
        3 遍历字符串
            不存在: list_chars.append(字符)  list_times.append(1)
            存在: char_index = list_chars.index(字符)  list_times[char_index] +=1
        4 遍历打印

    字典方式: {字符1: 次数, 字符2: 次数, ...}
        1 定义函数: count_char_times(string)
        2 创建1个字典: dict_char_times
        3 遍历字符串:
            不存在: dict_char_times[字符] = 1
            存在: dict__char_times[字符] += 1
        4 遍历打印

    字典: 更适合存储一对一关系的数据
'''

# 列表实现方式
# def count_char_times(string):
#     '''
#         统计字符及字符出现的次数
#     :param string: str, 字符串
#     :return: tuple, 存储字符和次数的2个列表的元组
#     '''
#     list_chars = []    # 存储字符(字符唯一)
#     list_times = []    # 存储字符出现的次数
#     for char in string:
#         if char not in list_chars:  # 判断字符不在存储字符的列表中
#             list_chars.append(char)   # 追加字符
#             list_times.append(1)      # 追加字符出现的次数
#         else:   # 字符在存储字符的列表中
#             char_index = list_chars.index(char)  # 从存储字符的列表中获取到字符的索引值位置
#             list_times[char_index] += 1  # 对应到次数列表中的索引值位置的次数值+1
#     return list_chars, list_times   # 返回存储字符与存储次数的2个列表
#
# def print_char_info(list_chars, list_times):
#     '''
#         打印字符及字符出现的次数
#     :param list_chars: list, 存储字符的列表
#     :param list_times: list, 存储次数的列表
#     :return: None
#     '''
#     # 方法1: 长度一致,基于索引值
#     # for i in range(len(list_times)):
#     #     print(f'字符:{list_chars[i]}出现的次数:{list_times[i]}')
#
#     # 方法2: zip函数
#     for t in zip(list_chars, list_times):
#         print(f'字符:{t[0]}出现的次数:{t[1]}')
#
# list1, list2 = count_char_times('java')
# print_char_info(list1, list2)


# 字典实现方式
def count_char_times(string):
    '''
        统计字符及字符出现的次数
    :param string: str, 字符串
    :return: dict, 存储字符及次数的字典
    '''
    dict_char_times = {}   # 存储字符及对应的次数
    for char in string:
        if char not in dict_char_times:  # 判断字符不在存储字符的字典表中
            dict_char_times[char] = 1    # 第1次出现,则存储字符及次数为1
        else:   # 字符在存储字符的字典中
            dict_char_times[char] += 1   # 存在,获取字符(key)对应的值,次数+1
    return dict_char_times

def print_char_times_info(dicts):
    '''
        打印字典中字符及次数信息
    :param dicts: dict,存储字符及次数的字典
    :return: None
    '''
    for char, times in dicts.items():
        print(f'字符:{char}出现的次数为:{times}')

dict_result = count_char_times('java')
print_char_times_info(dict_result)