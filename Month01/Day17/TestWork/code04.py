'''
4、分解质因数
    定义函数：输入一个大于1的数，打印出对应的结果，否则返回输入错误。
    输入：-4
    输出：输入错误
    输入：2
    输出：2 = 2 * 1
    输入：12
    输出：12 = 2 * 2 * 3

分析:
    1 定义函数: split_number(number)
    2 判断: number > 1
        0 打印: print(number, '= ')
        1 循环(遍历2-本身的数): range(2, number+1) --> x
        2 if number == 1: break
        3 while循环(number % x == 0):    8 % 2 == 0
            if number % x == 0:
                print('x', num, end='')
                number //= x
'''


def split_number(number):
    '''
        根据传入的整数分解因数
    :param number: int,分解整数
    :return: None
    '''
    if number > 1:
        print('{} = '.format(number), end='')
        for i in range(2, number + 1):
            if number == 1:
                break
            while number % i == 0:
                if number % i == 0:
                    print(i, end='')
                    number //= i
                if number != 1:
                    print(' x ', end='')
        else:
            print(' x 1', end='')
    else:
        print('输入错误')


split_number(4)
# split_number(7)
