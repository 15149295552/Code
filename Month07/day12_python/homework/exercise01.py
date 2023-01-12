# 定义函数,计算距离生日的天数
from datetime import datetime, timedelta


def get_day_by_birthday(month, day):
    """
        获取距离生日的天数
    :param month:月
    :param day:日
    :return:天数
    """
    current = datetime.now()
    birthday = datetime(current.year, month, day)
    if current > birthday:
        # 明年生日 - 当前日期
        return (birthday + timedelta(365) - current).days
    # 今年生日 - 当前日期
    return (birthday - current).days


print(get_day_by_birthday(1, 1))