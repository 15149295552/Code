'''
2、水仙花数
    定义函数：计算传入位数区间哪些是水仙花数，存储至列表中并打印。
    水仙花：表示各个位上的数对应次方的和等于该数。
    如：153 = 1 ** 3 + 5 ** 3 + 3 ** 3 （3位数: 对应3次方）
        1634 = 1 ** 4 + 6 * 4 + 3 ** 4 + 4 * * 4 （4位数: 对应4次方）

    输入：3 # 表示数区间：[100, 999]
    输出：[153, 370, 371, 407]
    输入：4 # 表示数区间：[1000, 9999]
    输出：[1634, 8208, 9474]

分析:
    1 定义函数: water_number(digit)
    2 定义列表: 存储水仙花数
    3 循环遍历:
        range(10**(digit-1), 10**digit)     # 3
        range(10**(digit-1), 10**digit)     # 4   --> number

        # 如何取出各个位上的数?    345
        0 定义变量, 累加计算的和
        1 转为字符串: '345'
        2 遍历字符串: '3'  '4'  '5'
        3 累加: int(字符) ** digit
        4 判断: 累加计算的和 == number --> 水仙花数
        5 存储水仙花数
    4 返回列表
'''


def water_number(digit):
    '''
        计算并存储指定位数范围内的水仙花数
    :param digit: int,位数
    :return: list, 存储水仙花数
    '''
    if digit > 2:
        list_numbers = []
        for i in range(10 ** (digit - 1), 10 ** digit):
            sums = 0
            for chr in str(i):
                sums += int(chr) ** digit

            if sums == i:
                list_numbers.append(i)

        return list_numbers


print(water_number(2))
print(water_number(3))
print(water_number(4))
print(water_number(6))
