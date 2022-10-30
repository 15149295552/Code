'''
19、二分法查找
    定义函数：在有序数字列表中找到目标值，并返回其索引。如果目标值不在列表中，返回它可以按顺序插入的索引。
    输入：[1,2,6,8,9]  8
    输出：3       # 返回存在数字8的索引值

    输入：[1,2,6,8,9]  5
    输出：2       # 返回不存在数字5的插入位置的索引值

分析：
    1 定义函数： search_insert_index(list_number, target)
    2 使用2个变量：记录最左侧、最右侧的位置（索引值）
    3 循环左侧的索引值与右侧的索引值比较：（left <= right）
        1 计算中间的索引值位置 mid = (left + right) // 2
        2 比较mid索引值对应的元素与目标值的大小关系
            等于： 目标值在序列中中间位置
                return mid
            小于： 目标值在序列右半区
                left = mid + 1
            大于： 目标值在序列左半区
                right = mid - 1
        3 没有此元素，则返回插入的位置： left
'''


def search_insert_index(list_number, target):
    '''
        在有序数字列表中找到目标值，并返回其索引
    :param list_number: list，有序列表
    :param target: int，目标值
    :return: int，元素索引值或插入索引值
    '''
    left = 0
    right = len(list_number) - 1
    while left <= right:
        mid = (left + right) // 2
        if list_number[mid] == target:
            return mid
        elif list_number[mid] < target:  # 中间偏由右半区（将左侧的位置移动到mid+1的位置）
            left = mid + 1
        else:   # 中间偏左半区（将右侧的位置移动到mid-1的位置）
            right = mid - 1
    return left

print(search_insert_index([1, 2, 6, 8, 9], 5))
print(search_insert_index([1, 2, 6, 8, 9], 7))
