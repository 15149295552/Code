'''
2048游戏代码实现
    核心功能
        左  move_left
        右  move_right
        上  move_up
        下  move_down

    游戏数据: 二维列表
        降维思想: 二维 --> 一维
            list_map = [
                [2, 0, 4, 2],
                [8, 8, 0, 2],
                [2, 2, 0, 2],
                [4, 0, 4, 4]
            ]

            line = [2, 0, 4, 2]

        左移: 列表的长度不变(4个)  --> [2, 4, 2, 0]
                [2, 0, 4, 2]
            --> [2, 4, 0, 2]
            --> [2, 4, 2, 0]   --> 0元素后移

    功能实现:
        1 0元素移动到末尾
            1 反向遍历每一行 --> 列表
            2 判断当前元素是否为0
                为0,删除该元素,同时在列表最后追加一个0

        2 相同元素合并
            1 0元素移动到末尾
            2 遍历每一行 --> 列表
                1 比较前后2个元素是否相同,并且元素如果不为0
                    前1个元素的结果: 当前元素 + 后一个元素
                    删除后1个元素
                    在列表最后再追加一个0

        3 左移
            1 遍历map  --> 每个小列表
                1 声明line 为全局变量 --> 修改之前定义全局的line --> marge函数中操作的全局变量line
                    line = 每一行  --> 小列表
                2 调用 相同元素合并的函数

        4 右移
            1 遍历map  --> 每个小列表
                1 声明line 为全局变量
                2 将每个小列表反向赋值给line
                3 调用 相同元素合并的函数
                4 切片赋值(反向填充) --> 将计算后的line结果赋值到小列表的反向结果中

        5 转置
            1 遍历map --> 行号
            2 遍历小列表 --> 列号
                行-->列, 列-->行:
                    将对角线上的元素互相交换位置(除了中心对称轴以外)

        6 上移
            1 转置 --> map列表
            2 基于左移函数实现元素合并
            3 转置 --> map列表

        7 下移
            1 转置 --> map列表
            2 基于右移函数实现元素合并
            3 转置 --> map列表

        8 计算空白位置
            空白位置: 元素为0
            1 将原有的map全部设置为0
            2 遍历map --> 每一行 --> 小列表 --> 行号
            3 遍历小列表 --> 列号
                1 判断元素是否等于0
                    等于0: 将空白位置 (行号, 列号) 存储到位置列表中
            4 返回位置列表

        9 随机选择空白位置
            方案1: 产生随机整数 --> 对应位置列表中的索引值 --> 随机 (行号, 列号)
            方案2: 使用random模块的choice方法随机选择一个 --> 随机 (行号, 列号)

            1 调用 计算空白位置 --> 位置列表
            2 随机选择
            3 返回空白位置 --> (行号, 列号)

        10 随机产生2或4
            要求: 产生2的概率为:90%, 产生4的概率为:10%
            方案1:从列表中随机选择一个,判断
                1 生成 [1, 10] 的列表
                2 random.choice(列表) --> 随机整数
                3 判断随机整数等于1, 返回4,否则返回2

            方案2:randint(1,10) 判断
                1 randint(1,10) --> 随机整数
                2 判断随机整数等于1, 返回4,否则返回2

        11 填充map中位置数据
            1 调用 随机选择空白位置 --> 随机空白位置 (行号, 列号)
            2 调用 随机产生2或4 --> 2 或 4
            3 通过索引修改map中对应位置的值 --> 随机产生了2或4

        12 判断游戏结束
            游戏不结束条件:
                1 有空白位置
                    1 调用 计算空白位置的函数 --> 空白位置列表
                        判断: 空白位置列表的长度 > 0:
                            return False

                2 能上下方向或左右方向移动
                    左右方向移动:
                        1 遍历map --> 行号
                            通过行号索引小列表 遍历 --> 列号
                            if map[行号][列号] == map[行号][列号+1]:
                                return False

                    上下方向移动:
                        1 遍历map --> 行号
                            通过行号索引小列表 遍历 --> 列号
                            if map[列号][行号] == map[列号+1][行号]:
                                return False

                return True

        13 游戏开始
            1 调用2次: 产生随机数的函数
            2 绘制界面

        14 绘制界面
            循环嵌套遍历 list_map

        15 用户选择
            输入: asad
                判断:调用对应的函数:move_up/down/left/right
            产生1个随机数
            调用: 判断游戏是否结束的函数
                if 函数返回值:   # True 结束
                    return 'over'

        16 主函数
            游戏开始
            while True:
                if 用户选择函数 == 'over':
                    break
                绘制map
'''

import random
import os

line = [0, 0, 4, 2]


def zero_to_end():
    '''
        0元素后移(反向遍历,判断是否为0,则删除,在列表末尾追加一个0)
    :return: None
    '''
    for i in range(len(line) - 1, -1, -1):
        if line[i] == 0:
            del line[i]
            line.append(0)


# zero_to_end()
# print(line)

def marge():
    '''
        相同元素合并(0元素移动到末尾[左移], 前1个元素是否与后一个元素相等,相等合并
                后一个元素删除,在列表末尾追加一个0)
    :return:
    '''
    zero_to_end()  # 0元素后移(将非0的元素移动到末尾,方便合并)
    for i in range(len(line) - 1):
        if line[i] == line[i + 1] and line[i] != 0:
            line[i] += line[i + 1]
            del line[i + 1]
            line.append(0)


# line = [4, 0, 4, 0]
# marge()
# print(line)

list_map = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


def move_left():
    '''
        左移(遍历二维列表 --> 每一行(一维的列表) --> 合并)
    :return: None
    '''
    for x in list_map:
        global line
        line = x  # 创建了局部变量(只能用在当前函数中)
        marge()


# move_left()
# print(list_map)

def move_right():
    '''
        右移(将每一行反向,基于合并(左移)操作,再反向)
    :return: None
    '''
    for x in list_map:
        global line
        line = x[::-1]
        marge()
        x[::-1] = line  # 切片赋值(反向填充)


# move_right()
# print(list_map)

def transpose():
    '''
        转置: 行变列,列变行
    :return: None
    '''
    for row in range(len(list_map) - 1):
        for col in range(row + 1, len(list_map)):
            list_map[row][col], list_map[col][row] = list_map[col][row], list_map[row][col]


# transpose()
#
# for x in list_map:
#     print(x)


def move_up():
    '''
        上移(转置,左移,转置)
    :return: None
    '''
    transpose()
    move_left()
    transpose()


# move_up()


def move_down():
    '''
        下移(转置,右移,转置)
    :return: None
    '''
    transpose()
    move_right()
    transpose()


# move_down()
# for x in list_map:
#     print(x)
def calculate_empty_location():
    '''
        计算并存储空白位置(元素为0的位置)
    :return: list, 存储空白位置
    '''
    list_empty_loc = []
    for row in range(len(list_map)):  # 遍历大列表的长度 --> 行号
        for col in range(len(list_map[row])):  # 遍历小列表的长度  --> 列号
            if list_map[row][col] == 0:
                list_empty_loc.append((row, col))
    return list_empty_loc


# print(calculate_empty_location())

def random_choice_empty_loc():
    '''
        随机选择一个空白位置(用于填充2或4)
            1 获取存储空白位置的列表
            2 随机选择一个空白位置
                随机产生一个[0, len(list_loc)-1] 的整数 --> 对应空白位置列表的索引值
                随机位置: list_loc[random_index]
    :return: tuple, 空白位置((行号, 列号))
    '''
    list_loc = calculate_empty_location()
    # print(list_loc)
    # 方法1:
    # random_index = random.randint(0, len(list_loc)-1)
    # return list_loc[random_index]

    # 方法2:
    return random.choice(list_loc)


# print(random_choice_empty_loc())


def randon_gender_two_or_four():
    '''
        随机产生2或4(2产生的概率: 90%, 4产生的概率: 10%)
    :return: int, 2或4
    '''
    # 方案1:
    # list_data = list(range(1, 11))
    # random_number = random.choice(list_data)
    #
    # if random_number != 1:
    #     return 2
    # else:
    #     return 4

    # 方案2:
    random_number = random.randint(1, 10)
    return 2 if random_number != 1 else 4


# print(randon_gender_two_or_four())

def modify_map_number():
    '''
        修改map中的值 (将随机产生的2或4 填充到 随机空白位置)
    :return: None
    '''
    empty_loc = random_choice_empty_loc()  # (行号, 列号)
    random_number = randon_gender_two_or_four()
    list_map[empty_loc[0]][empty_loc[1]] = random_number


# modify_map_number()
# modify_map_number()
# for line in list_map:
#     print(line)

def is_game_over():
    '''
        判断游戏是否结束
    :return: bool, 结束返回True,否则返回False
    '''
    # 1 判断有空白位置
    list_empty_loc = calculate_empty_location()
    if len(list_empty_loc) > 0:
        return False

    # 2 可横向或纵向移动
    # 横向移动
    # for row in range(len(list_map)):
    #     for col in range(len(list_map)-1):
    #         if list_map[row][col] == list_map[row][col+1]:
    #             return False
    #
    # # 纵向移动
    # for row in range(len(list_map)):
    #     for col in range(len(list_map)-1):
    #         if list_map[col][row] == list_map[col+1][row]:
    #             return False

    # 可横向或纵向移动
    for row in range(len(list_map)):
        for col in range(len(list_map) - 1):
            if list_map[row][col] == list_map[row][col + 1] or list_map[col][row] == list_map[col + 1][row]:
                return False

    return True


def start_game():
    '''
        开始游戏
    :return: None
    '''
    modify_map_number()
    modify_map_number()
    draw_map()


def draw_map():
    '''
        绘制map (4行4列)
    :return: None
    '''
    os.system('cls')
    for line in list_map:
        for iter in line:
            print(iter, end='\t')
        print()


def user_choice():
    '''
        用户选择 [输入:wsad]
    :return: str, 游戏结束返回'over',否则返回None
    '''
    choice = input('请输入[WSAD]: ').upper()
    if choice == 'W':
        move_up()
    elif choice == 'S':
        move_down()
    elif choice == 'A':
        move_left()
    elif choice == 'D':
        move_right()
    else:
        print('输入错误')

    modify_map_number()
    if is_game_over():
        return 'over'


def main():
    '''
        主函数
    :return: None
    '''
    start_game()
    while True:
        if user_choice() == 'over':
            break
        draw_map()


main()
