"""
    标准库
        time
"""
import time

# 时间戳(机器时间):从1970年元旦到现在经过的秒数
print(time.time())
# 时间元组(人类时间):从公元元年到现在
print(time.localtime())

# 时间戳 --> 时间元组(年,月,日,时,分,秒,星期,年的第几天,夏令时)
# 语法:时间元组 = time.localtime(时间戳)
tuple_time = time.localtime(-123454554)
print(tuple_time[0])
print(tuple_time[-3])
print(tuple_time[:3])
print(tuple_time[3:-3])

# 时间元组 --> 时间戳
# 语法:时间戳 = time.mktime( 时间元组 )
print(time.mktime(tuple_time))

# 时间格式化字符串
# 时间元组 --> 字符串
# 语法:字符串 = time.strftime(格式,时间元组)
print(time.strftime("%y/%m/%d %H:%M:%S", tuple_time))
print(time.strftime("%Y/%m/%d %H:%M:%S", tuple_time))
print(time.strftime("%Y年%m月%d日 %H时%M分%S秒", tuple_time))
print(time.strftime("%Y年 %S秒", tuple_time))

# 字符串 --> 时间元组
# 时间元组 = time.strptime(字符串,格式)
print(time.strptime("1966年02月02日 11时04分06秒", "%Y年%m月%d日 %H时%M分%S秒"))
















