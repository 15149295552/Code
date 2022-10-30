'''
    定义函数：输入一个终止数，计算该区间内有哪些素数？
        如：输入10（表示区间：2-10），则素数有：[2, 3, 5, 7]

分析：【跨函数调用】
    1 函数1：判断一个数是否素数
        1 判断当前的数是否大于1
            1 循环：range(2, 数) --> x：  # 找出2-该数之前是否还存在第3个因数
                判断：数 % x == 0:
                    return False
            2 该数是素数
                return True
        2 该数错误
            return False

    2 函数2：计算区间内哪些是素数
        0 创建列表用于存储素数
        1 循环：range(2, 终止数+1):
            if 判断一个数是否素数:
                素数列表.append(数)
        return 素数列表
'''
def is_prime(number):
    '''
        判断一个数是否素数
    :param number: int, 要判断的整数
    :return: bool，是素数则返回True，否则返回False
    '''

    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    return False

def save_prime(stop):
    '''
        计算区间哪些是素数
    :param stop: int，终止数
    :return: list，存储素数的列表
    '''
    list_prime = []
    for x in range(2, stop+1):
        if is_prime(x):
            list_prime.append(x)
    return list_prime


print(save_prime(10))
print(save_prime(2))
print(save_prime(-1))
