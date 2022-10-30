"""
month = int(input("请输入月:"))
day = int(input("请输入日:"))
days_of_month = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
total_days = sum(days_of_month[:month - 1])
total_days += day
print(f"{month}月{day}日是第{total_days}天.")

year = int(input("请输入年份:"))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
	day = 29
else:
	day = 28
"""


# -------------定义函数-------------
def get_total_day(year, month, day):  # 2
    february = get_february_day(year)  # 3
    days_of_month = (31, february, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    total_days = sum(days_of_month[:month - 1])
    total_days += day
    return total_days

def get_february_day(year):  # 4
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return 29
    return 28

# -------------调用函数-------------
print(get_total_day(2022, 9, 9))  # 1
