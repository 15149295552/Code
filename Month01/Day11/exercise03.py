# 练习1：定义函数, 根据年月日,计算星期。
# 输入：2020  9  15
# 输出：星期二

import time

def calculate_week(year, month, day):
    '''
        计算星期
    :param year:int, 年份
    :param month: int, 月份
    :param day: int, 天数
    :return: str, 星期数
    '''
    # 时间字符串 --> 时间元组
    time_tuple = time.strptime(f'{year}-{month}-{day}', '%Y-%m-%d')
    # print(time_tuple)
    week_index = time_tuple[-3]
    week_tuple = ('星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日')
    return week_tuple[week_index]

# print(calculate_week(2022, 8, 12))


# 练习2：定义函数，根据生日(年月日)，计算活了多天.
# 输入：2010  1  1
# 输出：从2010年1月1日到现在总共活了3910天
def life_days(year, month, day):
    '''
        计算出生到现在的总天数
    :param year:int, 年份
    :param month: int, 月份
    :param day: int, 天数
    :return: int, 总天数
    '''
    # 时间字符串 --> 时间元组
    time_tuple = time.strptime(f'{year}-{month}-{day}', '%Y-%m-%d')
    # 时间元组 --> 时间戳
    times = time.mktime(time_tuple)   # 1970.1.1 - 出生的总秒数
    # print(times)
    life_seconds = time.time() - times  # 出生的秒数 - 现在的秒数
    return int(life_seconds / 3600 / 24)

print(life_days(2000, 8, 12))   # 36600