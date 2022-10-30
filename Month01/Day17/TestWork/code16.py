'''
16、删除重复元素
  定义函数：根据传入的列表，判断列表中是否存在重复元素，存在则重复元素只保留1个，并返回删除的元素个数，如果列表中无重复元素则返回None。

    输入：[1, 3, 4, 1, 4, 4]
    输出：3      # 重复的元素有3个

    输入：[2, 4, 5, 7, 9]
    输出：None

分析：
    方法1：
        函数1 使用字典存储元素及次数
            0 定义函数：count_element_data(lists)
            1 判断列表的长度：len(lists) > 0
            2 创建字典： {字符:次数}
            3 遍历列表中的元素
                判断元素是否在字典中
                    不存在： [字符] = 1
                    存在： [字符] += 1
            4 返回存储数据的字典
        函数2 统计次数大于1的个数
            1 获取字典中value大于1的key (字符) --> [1, 4, 4]
            2 遍历：上述列表
                lists.remove(元素)
'''


def save_lists_data(lists):
    '''
        存储字符及次数
    :param lists: list，存储数据的列表
    :return: dict，存储字符及次数的字典
    '''
    if len(lists) > 0:
        dict_data = {}
        for item in lists:
            if item not in dict_data:
                dict_data[item] = 1
            else:
                dict_data[item] += 1
        return dict_data


dict_result = save_lists_data([1, 3, 4, 1, 4, 4])
print(dict_result)


def del_lists_items(dicts, lists):
    '''
        删除列表中重复的元素
    :param dicts: dict，存储字符及次数的字典
    :param lists: list，存储数据的列表
    :return: None
    '''
    lists_data = []
    for k, v in dicts.items():
        if v > 1:
            for i in range(v - 1):
                lists_data.append(k)
    # print(lists_data)

    for item in lists_data:
        lists.remove(item)
    return len(lists_data)

list01 = [1, 3, 4, 1, 4, 4]
print(del_lists_items(dict_result, list01))
print(list01)


# def del_shu(list01):
#     count = 0
#     for i in range(len(list01)):
#         for j in range(i + 1, len(list01)):
#             if list01[i] == list01[j]:
#                 count += 1
#     if count == 0:
#         return None
#     else:
#         return count - 1
#
#
# print(del_shu([1, 3, 3, 4, 1, 4, 4]))


def delete_duplicates(target):
    """
        删除重复元素并保持原来数据顺序
    :param target: list，表示可能存在重复元素的数据
    :return: int，删除元素的个数
    """
    if len(target) > 0 and len(target) != len(set(target)):
        count = 0
        for r in range(len(target) - 1, -1, -1):
            for c in range(r):
                if target[r] == target[c]:
                    del target[r]
                    count += 1
                    break
        return count

data = [1, 3, 4, 1, 4, 4]
print(delete_duplicates(data))
print(data)