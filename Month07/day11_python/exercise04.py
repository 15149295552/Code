"""
   练习2：定义函数，根据年月日,计算星期(星期一、星期二、星期三...星期日)
"""
from datetime import datetime


def calculate_week_name(year,month,day):
    week_number = datetime(year,month,day).weekday()
    tuple_week = ("星期一","星期二","星期三","星期四","星期五","星期六","星期日")
    return tuple_week[week_number]


print(calculate_week_name(1990, 1, 1))
