'''
3、星星菱形
    定义函数：输入任意大于2的边长，打印出对应的星星菱形。
    输入： 3      空格     星星
    输出： *       1       1
         ***      0       3
          *       1       1
    输入：5
    输出： *       2       1
         ***      1       3
        *****     0       5
         ***      1       3
          *       2       1

分析:
    最中间一行: 等于边长,上下对称, 组成: 空格 + 星星
    难点: 找到空格与星星之间的关系

    实现方案1: 2个for循环
        第 1 for循环: range(1, side+1, 2)  生成上半区星星
        第 2 for循环: range(side-2, 0, -2) 生成下半区星星

    实现方案2: 1个for循环
        1 计算边长的1半: side//2
        2 循环: range(-side//2, side//2+1)
            1 将数转为正数: 计算绝对值
            2 计算空格与星星的数量
                ' ' * 数
                '*' * (边长 - 2 * 数)
'''


# side = 5
# for x in range(1, side + 1, 2):
#     print(' ' * ((side - x) // 2) + '*' * x)
# for y in range(side - 2, 0, -2):
#     print(' ' * ((side - y) // 2) + '*' * y)
#
# for x in range(1, side, 2):
#     print(' ' * ((side - x) // 2) + '*' * x)
# for y in range(side, 0, -2):
#     print(' ' * ((side - y) // 2) + '*' * y)

def round_trangle(side):
    '''
        打印对应边长的星星菱形
    :param side: int,边长
    :return: None
    '''
    if side > 2:
        half = side // 2
        for x in range(-half, half + 1):
            x = -x if x < 0 else x
            space = ' ' * x
            star = '*' * (side - 2 * x)
            print(space + star)

round_trangle(2)
# round_trangle(3)
# round_trangle(5)
# round_trangle(9)
round_trangle(8)