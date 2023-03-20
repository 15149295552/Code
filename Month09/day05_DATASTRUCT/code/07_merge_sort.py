"""
归并排序
"""


def merge_sort(li):
    # 递归出口
    if len(li) == 1:
        return li

    # 1.先拆分
    mid = len(li) // 2
    left = li[:mid]
    right = li[mid:]
    # 递归思想
    left_li = merge_sort(left)
    right_li = merge_sort(right)

    # 合并
    return sort(left_li, right_li)


def sort(left_li, right_li):
    """
    :param left_li: 有序列表
    :param right_li: 有序列表
    :return: 合并后的有序列表
    """
    # [5, 8]  [3, 4]
    result = []
    while left_li and right_li:
        if left_li[0] > right_li[0]:
            result.append(right_li.pop(0))
        else:
            result.append(left_li.pop(0))

    # 循环结束,一个列表为空
    result += left_li
    result += right_li

    return result


if __name__ == '__main__':
    li = [6, 5, 3, 1, 8, 7, 2, 4]
    print(merge_sort(li))

    # print(sort([5, 8], [3, 4])) # [3,4,5,8]
    # print(sort([5, 8, 10], [3, 4])) # [3,4,5,8,10]








