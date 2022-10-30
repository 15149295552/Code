'''
定义函数：根据传入的列表及目标数，若该列表中存在对应2个数的和与目标值相同，则返回2个数在列表中的索引值，存在2组或多组2个数的和等于该目标数，则以第一组为准，反之，若列表中无2个数的和，无与目标数相等，则返回None
   输入：[1, 3, 2, 2, 4]    4
   输出：[0, 1]     # 对应列表中的数：1 与 3 的索引值
   输入：[1, 3, 2, 2, 4]    8
   输出：None
   输入：[1, 5, 2, 6, 7]    11
   输出：[1, 3]     # 对应列表中的数：5 与 6 的索引值

分析：
    方法1：
        1 遍历列表：range(len(lists)) --> i
            1 遍历列表： range(i+1, len(lists)) --> j
                if lists[i] + lists[j] == target:
                    return [i, j]

    方法2：
        1 遍历列表：range(len(lists)) --> i
            other = target - list[i]
            if other in lists:
                other_index = list.index(other)
                if i != other_index:
                    return [i, other_index]
'''


# 方法1
def find_sum_index(lists, target):
    '''
        查找列表中元素的和与目标数相等的2个元素的索引值
    :param lists: list，目标列表
    :param target: int，目标数
    :return: list，存在则返回索引值列表，否则返回None
    '''
    for i in range(len(lists)):
        for j in range(i + 1, len(lists)):
            if lists[i] + lists[j] == target:
                return [i, j]


# 方法2
def find_sum_index(lists, target):
    '''
        查找列表中元素的和与目标数相等的2个元素的索引值
    :param lists: list，目标列表
    :param target: int，目标数
    :return: list，存在则返回索引值列表，否则返回None
    '''
    for i in range(len(lists)):
        other = target - lists[i]
        if other in lists:
            other_index = lists.index(other)
            if i != other_index:
                return [i, other_index]


print(find_sum_index([1, 3, 2, 2, 4], 4))
print(find_sum_index([1, 3, 2, 2, 4], 8))
print(find_sum_index([1, 5, 2, 6, 7], 11))
'''
输入：[1, 3, 2, 2, 4]    4
输出：[0, 1]     # 对应列表中的数：1 与 3 的索引值
输入：[1, 3, 2, 2, 4]    8
输出：None
输入：[1, 5, 2, 6, 7]    11
输出：[1, 3]     # 对应列表中的数：5 与 6 的索引值
'''
