'''
定义函数，根据年月日计算是这一年的第几天.
  要求：对输入天数根据月份进行验证
    如：2月天数必须在1-28/29之间
         1 3 5 7 8 10 月天数必须在1-31之间

分析：【跨函数调用】
    1 函数1：判断天数输入是否正确 --> 月份
        1 判断是否在 (1, 3, 5, 7, 8, 10, 12)
            if 0 < day <= 31:
                return True
            return False

        2 判断是否在 (4, 6, 9, 11)
            if 0 < day <= 30:
                return True
            return False

        3 判断是否等于2月
            if 0 < day <= 29:
                    return True
            return False

    2 函数2：计算闰年
        1 根据条件判断是否为闰年
            是：return True
            否：return False

    3 函数3：计算总天数
        1 判断年月日是否正确
            if 0 < year and 1 <= month <= 12 and 调用判断月份是否正确的函数:
                2 计算天数
                    1 判断是否等于 1
                        total_days = day
                    2 判断是否等于 2
                        total_days = 31 + day
                    3 判断是否大于 2
                        total_days = day
                        tuple_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30)
                        if 调用判断是否为闰年的函数:
                            total_days += 1
                        total_days += sum(tuple_day[:month-1])
'''


def is_leap_year(year):
    '''
        判断年份是否正确
    :param year: int，年份
    :return: bool，是闰年则返回True，否则返回False
    '''
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False


def juage_month_is_true(year, month, day):
    '''
        判断月份对应的天数是否正确
    :param year: int, 年份
    :param month: int, 月份
    :param day: int, 天数
    :return: bool，正确则返回True，否则返回False
    '''
    if month in (1, 3, 5, 7, 8, 10, 12):
        if 0 < day <= 31:
            return True
    if month in (4, 6, 9, 11):
        if 0 < day <= 30:
            return True
    if month == 2:
        if is_leap_year(year):
            if 0 < day <= 29:
                return True
        else:
            if 0 < day <= 28:
                return True

    return False


def calculate_total_days(year, month, day):
    '''
        计算给定的日期是当年的第多少天
    :param year: int, 年份
    :param month: int, 月份
    :param day: int, 天数
    :return：int, 总天数
    '''
    if year > 0 and 1 <= month <= 12 and juage_month_is_true(year, month, day):
       if month == 1:
           return day
       elif month == 2:
           return 31 + day
       else:  # 12 >= month >= 3
           total_days = day
           tuple_day = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30)
           if is_leap_year(year):
               total_days += 1
           total_days += sum(tuple_day[:month - 1])
           return total_days


print(calculate_total_days(2022, 8, 8))
print(calculate_total_days(-2022, 2, 30))
