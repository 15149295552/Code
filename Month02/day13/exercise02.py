"""
    练习1：定义函数,根据年月日,计算星期。
    输入：2020  9  15
    输出：星期二
"""
import time


def calculate_week_name(year, month, day):
    """

    :param year:
    :param month:
    :param day:
    :return:
    """
    # 年月日 --> 字符串
    # str_time = "%s-%s-%s"%(year, month, day)
    str_time = f"{year}-{month}-{day}"
    # 字符串 --> 时间元组
    tuple_time = time.strptime(str_time, "%Y-%m-%d")
    # 时间元组 --> 星期数
    week_number = tuple_time[-3]
    # 星期数 --> 星期名称
    tuple_week = ("星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日")
    return tuple_week[week_number]

print(calculate_week_name(2020, 9, 15))

# 练习2：定义函数,根据生日(年月日),计算活了多天.
# 输入：2010  1  1
# 输出：从2010年1月1日到现在总共活了3910天
#
#  年月日 -> 字符串
#  字符串 -> 出生的时间元组
#  出生的时间元组 -> 出生的时间戳
#  现在的时间戳 - 出生的时间戳  -> 活的秒
#  活的秒 -> 活的天