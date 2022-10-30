# 作业
#     1 整理今日课程内容
#     2 作业1：
#         # 商品字典
# dict_commodity_infos = {
#     1001: {"name": "屠龙刀", "price": 10000},
#     1002: {"name": "倚天剑", "price": 10000},
#     1003: {"name": "金箍棒", "price": 52100},
#     1004: {"name": "口罩", "price": 20},
#     1005: {"name": "酒精", "price": 30},
# }
# #         # 订单列表
# list_orders = [
#     {"cid": 1001, "count": 1},
#     {"cid": 1002, "count": 3},
#     {"cid": 1005, "count": 2},
# ]


#         1. 打印所有商品信息,
#            格式：商品编号xx,商品名称xx,商品单价xx.
# def func_dict(dict):
#     for k, v in dict.items():
#         print(f'商品编号{k}，商品名称{v["name"]}，商品单价{v["price"]}')
#
#
# func_dict(dict_commodity_infos)


#         2. 打印所有订单中的信息,
#            格式：商品编号xx,购买数量xx.
# def func_list(list):
#     for i in list:
#         print(f'商品编号{i["cid"]}，购买数量{i["count"]}')
#
#
# func_list(list_orders)


#         3. 打印所有订单中的商品信息,
#            格式：商品名称xx,商品单价:xx,数量xx.


# def print_order_commodity_infos():
#     for order in list_orders:
#         code = order['cid']
#         commodity = dict_commodity_infos[code]
#         print(f'商品名称：{commodity["name"]}，商品单价{commodity["price"]},商品数量{order["count"]}')
#
#
# print_order_commodity_infos()
#         4. 查找数量最多的订单(使用自定义算法,不使用内置函数)
# def func_max(list):
#     a = 0
#     for i in list:
#         if i.get("count") > a:
#             a = i.get("count")
#             b = i.get("cid")
#     print(f'数量最多的订单{b}')
#
#
# func_max(list_orders)
# #         5. 根据购买数量对订单列表降序(大 --> 小)排列
# # def func_sort(list):
# #     lists = sorted(list, key=lambda x: x["count"], reverse=True)
# #     print(lists)
# #
# #
# # func_sort(list_orders)
# def order_count_desc():
#     for i in range(len(list_orders) - 1):
#         for j in range(i + 1, len(list_orders)):
#             if list_orders[i]['count'] == list_orders[j]['count']:
#                 list_orders[i], list_orders[j] = list_orders[j], list_orders[i]
#
#
# order_count_desc()
# print(list_orders)
# 3 作业2
#         定义函数，根据年月日计算是这一年的第几天.
#           要求：对输入天数根据月份进行验证
#             如：2月天数必须在1-28/29之间
#                  1 3 5 7 8 10 月天数必须在1-31之间
# def is_leap_year(year):
#     '''
#     判断年份是否正确
#     :param year:
#     :return:
#     '''
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#         return True
#     return False
#
#
# def juage_month_is_true(year, month, day):
#     '''
#     判断月份对应的天数是否正确
#     :param year:
#     :param month:
#     :param day:
#     :return:
#     '''
#     if month in (1, 3, 5, 7, 8, 10, 12):
#         if 0 < day <= 31:
#             return True
#         if month in (4, 6, 9, 11):
#             if 0 < day <= 30:
#                 return True
#         if month == 2:
#             if is_leap_year(year):
#                 if 0 < day <= 29:
#                     return
#                 else:
#                     if 0 < day <= 28:
#                         return True
#         return False
#
#
# def calculate_total_days(year, month, day):
#     '''
#     计算给定的日期是当年的第多少天
#     :param year:
#     :param month:
#     :param day:
#     :return:
#     '''
#     if year > 0 and 1 <= month <= 12 and juage_month_is_true(year, month, day):
#         if month == 1:
#             return day
#         elif month == 2:
#             return 31 + day
#         else:
#             total_days = day
#             tuple_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
#             if is_leap_year(year):
#                 total_days += 1
#             total_days += sum(tuple_day[:month - 1])
#             return total_days
#
#
# print(calculate_total_days(2022, 8, 8))
#     4 作业3
#         定义函数：输入一个终止数，计算该区间内有哪些素数？
#             如：输入10（表示区间：2-10），则素数有：[2, 3, 5, 7]
# def is_prime(num):
#     '''
#     判断一个数是否素数
#     :param num:
#     :return:
#     '''
#     if num > 1:
#         for i in range(2, num):
#             if num % i == 0:
#                 return False
#             return True
#         return False
#
#
# def save_prime(stop):
#     list_prime = []
#     for x in range(2, stop):
#         if is_prime(x):
#             list_prime.append(x)
#     return list_prime
#
#
# print(save_prime(10))
# 5 作业4
#         定义函数：根据传入的列表及目标数，若该列表中存在对应2个数的和与目标值相同，则返回2个数在列表中的索引值，存在2组或多组2个数的和等于该目标数，则以第一组为准，反之，若列表中无2个数的和，无与目标数相等，则返回None
#        输入：[1, 3, 2, 2, 4]    4
#        输出：[0, 1]     # 对应列表中的数：1 与 3 的索引值
#        输入：[1, 3, 2, 2, 4]    8
#        输出：None
#        输入：[1, 5, 2, 6, 7]    11
#        输出：[1, 3]     # 对应列表中的数：5 与 6 的索引值
# def find_sum_index(lists, target):
#     '''
#     查找列表中元素的和与目标数相等的2个元素的索引值
#     :param lists:
#     :param target:
#     :return:
#     '''
#     for i in range(len(lists)):
#         for j in range(i + 1, len(lists)):
#             if lists[i] + lists[j] == target:
#                 return [i, j]
#
#
# find_sum_index()
def find_sum_index(lists, target):
    for i in range(len(lists)):
        other = target - lists[i]
        if other in lists:
            other_index = lists.index(other)
            if i != other_index:
                return [i, other_index]
