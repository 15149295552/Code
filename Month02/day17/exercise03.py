"""
练习2：为sum_data,增加打印函数执行时间的功能.
​    函数执行时间公式： 执行后时间 - 执行前时间
"""
import time


def print_execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs) # 调用旧功能
        stop = time.time()
        print(f"执行时间:{stop - start}")
        return res

    return wrapper


@print_execution_time  # 调用外函数
def sum_data(n):
    sum_value = 0
    for number in range(n):
        sum_value += number
    return sum_value


print(sum_data(10))  # 调用内函数
print(sum_data(1000000))
