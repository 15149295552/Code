'''
15、素数
 定义函数，实现以下判断：
  （1）传入1个参数，判断是否为素数，是则返回True，不是则返回False。

分析：
    素数，因数只有1与本身的整数(最小的素数是2)。
    规则：除了1与本身以外，若还存在第3个因数，则该数就不是因数
    实现：
        1 定义函数：is_prime(number)
            1 判断： number > 1
                1 遍历：range(2 , number)  -->x
                    if number % x == 0:
                        return False
                2 else: return True
'''


def is_prime(number):
    '''
        判断一个整数是否为素数
    :param number: int，判断的整数
    :return: bool，是则返回True，不是则返回False
    '''
    if number > 1:
        for x in range(2, number):
            if number % x == 0:
                return False
        return True


#
#
# print(is_prime(2))
# print(is_prime(3))
# print(is_prime(9))
# print(is_prime(121))


# （2）判断区间内哪些是素数，将其存储值列表并打印。
'''
分析
    1 定义函数：prime_mn(m, n):
        1 判断m与n的大小关系
            m < n: 不用变化
            m > n: 交换：序列赋值
        2 创建列表，存储素数
        3 遍历区间内的整数： range(m, n) -->x
            1 调用判断一个数是否为素数的函数： is_prime(x)
                返回True: 是素数，添加至列表中
        4 返回列表
'''


def prime_mn(m, n):
    '''
        计算并存储区间内的素数
    :param m: int，起始值
    :param n: int，终止值
    :return: list，存储素数的列表
    '''
    if m > n:
        m, n = n, m
    list_prime = []
    for x in range(m, n):
        if is_prime(x):
            list_prime.append(x)
    return list_prime


# print(prime_mn(1, 20))
# print(prime_mn(20, 2))


# （3）传入1个终止数（不包含），返回0到该终止数之间的所有素数列表并打印。
'''
分析：
    1 定义函数： save_onlyone_prime(stop)
        1 判断 stop > -1
            1 调用 prime_mn(0, stop)
            2 返回 prime_mn 函数的返回值（list）
'''

def save_onlyone_prime(stop):
    '''
        返回终止数区间内的所有素数
    :param stop: int，终止数
    :return: list，存储素数的列表
    '''
    if stop > -1:
        return prime_mn(0, stop)

print(save_onlyone_prime(30))