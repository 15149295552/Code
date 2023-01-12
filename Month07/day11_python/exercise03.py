"""
    练习1：定义函数，根据生日(年月日)，计算活了多天
"""
# 自动生成导入代码：alt + 回车
from datetime import datetime, timedelta


def calculate_life(year, month, day):
    """

    :param year:
    :param month:
    :param day:
    :return:
    """
    delta = datetime.now() - datetime(year, month, day)
    return delta.days


print(calculate_life(1990, 1, 1))  # 12035
