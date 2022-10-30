'''
14、查找元素
   定义函数：给定一个整数列表和目标整数值，从列表中找出2个整数之和与目标值相同，存着则返回2个整数在列表中对应的索引值，不存在则返回None；若列表中同一个元素只能使用1次，若存在多种情况满足则仅返回第1中情况。

    输入：[4, 5, 3, 6]  10
    输出：0 3       #  10 = 4 + 6   不能取 10 = 5 + 5

    输入：[1, 4, 6, 2, 7]  12
    输出：None

分析：
    1 定义函数： find_element(lists, target)
    2 判断列表长度：len(lists) > 1
        1 遍历列表： range(len(lists))  --> x
        2 计算另一个数： other = target - x
        3 判另一个数是否在列表中： other in lists
            1 计算元素的索引值： lists.index(other) --> index
            2 判断 index ！= x
                return x, index
'''


def find_element(lists, target):
    '''
        查看列表2个元素之和等于目标值
    :param lists: list，存储元素的列表
    :param target: int，目标整数
    :return: tuple，元素的索引值
    '''
    if len(lists) > 1:
        for x in range(len(lists)):
            other = target - lists[x]
            if other in lists:
                index = lists.index(other)
                if index != x:
                    return x, index


print(find_element([4, 4, 3, 6], 8))
print(find_element([4, 5, 3, 6], 10))
print(find_element([1, 4, 6, 2, 7], 12))
