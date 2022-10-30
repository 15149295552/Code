'''
17、第一个不重复元素
    定义函数：返回字符串中第一个不重复的字符，不存在重复则返回None。
    输入：'ABCACDBEFD'
    输出：'E'

    输入：'ABCDEF'
    输出：None

分析：
    方法1：基于切片判断
        1 定义函数1： 使用字典存储字符及字符出现的次数
        2 定义函数2：遍历字符串，与字典中的字符对应值比较，如果次数为1，则表示是第一个不重复的元素
'''

def first_not_repeating_char(target):
    '''
        获取第1个不重复的元素
    :param target: str, 目标字符串
    :param list_char: list, 存储字符的列表
    :param list_times: list, 存储次数的列表
    :return: object, 符合条件的目标结果
    '''
    if len(target) == 1:
        return target
    else:
        dict_result = save_string_infos(target)
        for c in target:
            if dict_result[c] == 1:
                return c

def save_string_infos(string):
    '''
        存储字符及字符出现的次数
    :param string: str, 判断的字符串
    :return: dict,存储字符及出现次数的字典
    '''
    dict_chars = {}
    for s in string:
        if s not in dict_chars:
            dict_chars[s] = 1
        else:
            dict_chars[s] += 1
    return dict_chars


def first_not_repeating_char(string):
    '''
        获取第1个不重复的元素
    :param string: str, 目标字符串
    :return: object, 符合条件的目标结果
    '''
    if len(string) == 1:
        return string
    else:
        for c in string:
            if string.count(c) == 1:
                return c

print(first_not_repeating_char("ABCACDBEFD"))
print(first_not_repeating_char("ABCD"))
print(first_not_repeating_char("BBCC"))