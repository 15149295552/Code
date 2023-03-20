"""
快速排序
"""


def quick_sort(li, first, last):
    """
    快速排序逻辑
    :param li: 无序列表
    :param first: 基准值索引
    :param last: 右游标索引
    :return:
    """
    # 递归出口
    if first > last:
        return

    index = sort(li, first, last)
    # 递归思想
    quick_sort(li, first, index - 1)
    quick_sort(li, index + 1, last)


def sort(li, first, last):
    """
    :param li: 无序列表
    :param first: 基准值索引
    :param last: 右游标索引
    :return:
    """
    lcur = first + 1
    rcur = last

    while True:
        # 左游标右移
        while lcur <= rcur and li[lcur] <= li[first]:
            lcur += 1

        # 右游标左移
        while lcur <= rcur and li[rcur] >= li[first]:
            rcur -= 1

        if lcur > rcur:
            # 右游标和基准值互换位置
            li[rcur], li[first] = li[first], li[rcur]
            return rcur
        else:
            # 左右游标互换位置
            li[lcur], li[rcur] = li[rcur], li[lcur]


if __name__ == '__main__':
    li = [6, 5, 3, 1, 8, 7, 2, 4]
    quick_sort(li, 0, len(li) - 1)
    print(li)


















