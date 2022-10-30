# 练习2：打印20个斐波那契数列（1 1 2 3 5 8 13 21）。
'''
分析：
    1 列表存储：[1, 1]
    2 定义函数：
        计算一个斐波那契数
'''

# list_numbers = [1, 1]
#
# for i in range(18):
#     list_numbers.append(list_numbers[i] + list_numbers[i+1])
#
# print(list_numbers, len(list_numbers))



def fbnq(n):
    '''
        计算指定位置的个数的斐波那契数
    :param n: int，第几个
    :return: int，计算的斐波那契数
    '''
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fbnq(n-1) + fbnq(n-2)

list_numbers = [1, 1]
for i in range(3, 21):
    res = fbnq(i)
    list_numbers.append(res)

print(list_numbers)
# print(fbnq(6))
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
