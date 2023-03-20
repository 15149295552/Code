"""
    python实现二分查找
"""


def binary_search(li, item):
    """
    :param li: 有序数组
    :param item: 查找的元素
    :return: True | False
    """
    low = 0
    high = len(li) - 1

    while low <= high:
        mid = (low + high) // 2
        if li[mid] < item:
            low = mid + 1
        elif li[mid] > item:
            high = mid - 1
        else:
            return True

    return False


if __name__ == '__main__':
    li = [1, 2, 3, 4, 5, 6, 7, 8]
    print(binary_search(li, 4))





