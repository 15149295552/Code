'''
5、数字三角形
    定义函数：输入大于0 的数，打印出对应高度的数字三角形。
    输入：1
    输出：1
    输入：4
    输出：1 123 12345 1234567
    输入：6
    输出：1 123 12345 1234567 123456789 12345678901

分析:
    知识点: for循环嵌套
    1 定义函数: number_trangle(side)
    2 判断边长(side)大于0
                start     stop     step
        外层(x)    1       side+1     1
        内层(y)    1        2x        1      数字
                                            空白(side-x)
'''


def number_trangle(side):
    '''
        根据边长生成对应的数字三角形
    :param side: int,边长
    :return: None
    '''
    if side > 0:
        for x in range(1, side + 1):   # 控制行
            print(' ' * (side - x), end='')   # 打印每行左边的空格
            for y in range(1, 2 * x):   # 控制列
                print(y % 10, end='')   # 打印每列的数
            print()   # 换行


number_trangle(5)    # 9   side * 2 - 1
number_trangle(1)
number_trangle(8)    # 15  side * 2 - 1
