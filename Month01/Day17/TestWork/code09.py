'''
9、百元买百鸡
    定义函数：假设大鸡5元一只，中鸡3元一只，小鸡1元三只，现有100元，可以有多少种买法？

分析: 钱数: 100  只数: 100
    1 定义函数: buy_chicken
    2 计算只数及价格
        定义变量,记录卖法
        循环: 计算大鸡的数量
            循环: 计算中鸡的数量
                计算小鸡的数量 = 100 - 大鸡数量 - 中鸡数量
                判断: 大鸡数量 * 5 + 中鸡数量 * 3 + 小鸡数量 * 1/3 == 100:
                    变量 += 1
                    print(买鸡的信息)
'''


# def buy_chicken():
#     '''
#         计算买鸡的买法
#     :return: None
#     '''
#     times = 0
#     for big in range(21):   # 100 // 5 + 1  --> 大鸡数量
#         for mid in range(34):    # 100 // 3 + 1  --> 中鸡数量
#             small = 100 - big - mid    # 小鸡数量
#             if big * 5 + mid * 3 + small / 3 == 100:  # 若总价为100元.打印买法
#                 times += 1
#                 print(f'第{times}买法: 大鸡:{big}只, 中鸡:{mid}只, 小鸡:{small}只')
#
# buy_chicken()


def buy_chicken(money, count):
    '''
        计算买鸡的买法
    :param money: int, 钱数
    :param count: int, 总个数
    :return: None
    '''
    times = 0
    for big in range(money // 5 + 1):  # money // 5 + 1  --> 大鸡数量
        for mid in range(money // 3 + 1):  # money // 3 + 1  --> 中鸡数量
            small = count - big - mid  # 小鸡数量
            if big * 5 + mid * 3 + small / 3 == money:  # 若总价为100元.打印买法
                times += 1
                print(f'第{times}买法: 大鸡:{big}只, 中鸡:{mid}只, 小鸡:{small}只')


buy_chicken(200, 100)
