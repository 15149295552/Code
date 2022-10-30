# 练习2：为sum_data,增加打印函数执行时间的功能.
# ​    函数执行时间公式： 执行后时间 - 执行前时间
import time

# 装饰器函数
def exeture_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        times = time.time() - start_time
        print('原函数执行的时间:', times)
        return result

    return wrapper

@exeture_time
def sum_data(n):  # 原函数
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value

@exeture_time
def sum_data1(n):  # 原函数
    sum_value = 0
    x = 0
    while x < n:
        sum_value += x
        x += 1
    return sum_value

print(sum_data(10))
print(sum_data1(10))
print(sum_data(1000000))
print(sum_data1(1000000))