"""
    将局部变量改为全局变量
"""
# -------------全局变量-------------
year, month, day = 2022, 9, 9


# -------------定义函数-------------
def get_total_day():  # 2
    february = get_february_day()  # 3
    days_of_month = (31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    total_days = sum(days_of_month[:month - 1])
    total_days += day
    return total_days


def get_february_day():  # 4
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 29
    return 28


# -------------调用函数-------------
print(get_total_day())