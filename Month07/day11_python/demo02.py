"""
    时间日期模块
        对象与对象数据不同
        类与类行为不同
"""
from datetime import datetime, timedelta

# 一、datetime日期时间类
# 1.创建固定日期：年,月,日,时,分,秒
d1 = datetime(2022, 12, 14, 19, 15, 6)

# 2.获取星期
# 注意：星期一....星期日
#       0 ...   6
print(d1.weekday())

# 3.当前日期
d2 = datetime.now()
# 注意：通过实例变量获取数据
print(d2.year)
print(d2.month)
print(d2.day)
print(d2.hour)
print(d2.minute)
print(d2.second)

# 4.格式化字符串
# 时间 --> 字符串
# 语法：字符串 = datetime对象.strftime(格式)
# print(d2.strftime("%y/%m/%d %H:%M:%S"))
# print(d2.strftime("%y年%m月%d日 %H时%M分%S秒"))
print(d2.strftime("%Y年%m月%d日 %H时%M分%S秒"))
# 2022年12月14日 14时38分18秒

# 字符串 --> 时间
# datetime对象 = datetime.strptime(字符串,格式)
print(datetime.strptime("2022年12月14日 14时38分18秒", "%Y年%m月%d日 %H时%M分%S秒"))

# 二、timedelta 时间间隔类
# 1. 日期时间相减
delta1 = datetime.now() - datetime(2022, 11, 30, 14)
print(delta1)
print(delta1.days)  # 总天数
print(delta1.seconds)  # 天数以外的秒数

# 2. 日期时间 + 时间间隔
print(datetime.now() + timedelta(1))  # 明天
print(datetime.now() + timedelta(seconds=5))  # 5秒以后
print(datetime.now() + timedelta(minutes=2))  # 2分钟以后
print(datetime.now() + timedelta(weeks=1))  # 2分钟以后
