'''
18、杨辉三角
    创建函数，生成指定行数的杨辉三角。
'''


def get_yang_hui_triangle(row_count):
    """
        获取杨辉三角
    :param row_count: int, 行数
    :return: list, 存储杨辉三角列表
    """
    triangle = []
    for row_index in range(row_count):
        row = [None] * (row_index + 1)
        row[0], row[-1] = 1, 1
        for i in range(1, row_index):
            row[i] = triangle[row_index - 1][i - 1] + triangle[row_index - 1][i]
        triangle.append(row)
    return triangle


def yang_hui_triangle(row_count):
    """
        打印杨辉三角
    :param row_count: int, 行数
    :return: None
    """
    list_result = get_yang_hui_triangle(row_count)
    for item in list_result:
        # print(str(item).center(3 * len(list_result[-1])))
        print(' '.join(list(map(str, item))).center(3 * len(list_result[-1])))


yang_hui_triangle(6)
