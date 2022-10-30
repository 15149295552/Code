'''
12、数字阶乘
    定义函数：输入一个数，计算从1的阶乘，一直加到该数的阶乘，并打印出其和。
        输入：5
        输出：153      # 1! + 2! + 3! + 4! + 5!

分析：
    1 定义函数1：计算某个数的阶乘
        calculate_number_of_factorial(number)
            result = 1
            for n in range(1, number+1):
                result *= n
            return result
    2 定义函数2： 计算区间内所有数的阶乘和
        calculate_number_of_factorial_sum(stop)
            if stop >= 1:
                sums = 0
                for i in range(1, stop+1):
                    sums += calculate_number_of_factorial(i)
                return sums
'''


# 方法1：使用2个函数分别计算阶乘
# def calculate_number_of_factorial(number):
#     '''
#         计算指定数的阶乘
#     :param number: int，要计算的数
#     :return: int，阶乘结果
#     '''
#     result = 1
#     for n in range(1, number+1):
#         result *= n
#     return result

# print(calculate_number_of_factorial(5))

# def calculate_number_of_factorial_sum(stop):
#     '''
#         计算指定区间内所有数的阶乘和
#     :param stop: int，终止数
#     :return: int，阶乘和
#     '''
#     if stop >= 1:
#         sums = 0
#         for i in range(1, stop+1):
#             sums += calculate_number_of_factorial(i)
#         return sums
#
# print(calculate_number_of_factorial_sum(5))


# 方法2：使用for循环嵌套
def calculate_number_of_factorial_sum(stop):
    '''
        计算指定区间内所有数的阶乘和
    :param stop: int，终止数
    :return: int，阶乘和
    '''
    if stop >= 1:
        sums = 0   # 记录阶乘的和
        for i in range(1, stop + 1):   # 遍历区间的数
            result = 1  # 计算某个数的阶乘
            for n in range(2, i + 1):   # 计算某个数的阶乘
                result *= n
            sums += result    # 累加某个数的阶乘和
        return sums

print(calculate_number_of_factorial_sum(5))