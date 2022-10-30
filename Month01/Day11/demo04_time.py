# time - 关于时间的相关的操作
import time

# 1、时间戳: 从1970年1月1日 0时0分0秒到此刻的秒数
print(time.time())
# 作用: 1 计算程序的运行的时间   2 爬虫使用时间戳进行数据加密

# 时间元组
print(time.localtime())
print('过去的天数:', time.localtime()[-2])
print('过去的天数:', time.localtime().tm_yday)

# 时间元组 --> 时间戳
print(time.mktime(time.localtime()))

# 时间戳 --> 时间元组
print(time.gmtime(1000000000))

# 时间字符串
print(time.strftime('%Y/%m/%d %H:%M:%S %A'))

# 时间字符串 --> 时间元组
print(time.strptime('2008/8/8 10:08:08', '%Y/%m/%d %H:%M:%S'))

# 休眠
time.sleep(3)   # 休息3秒