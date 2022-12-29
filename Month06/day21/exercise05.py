'''
5.整数反转
   给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果,如果反转后整数超过 32 位的有符号整数的范围 [−231, 231 − 1] ，就返回 0。假设环境不允许存储 64 位整数（有符号或无符号）。
'''

'''
分析：
    1 如果该数为0，直接返回0
    2 如果不是0（该数需要反转）
        2.1 直接将整数转为传入的字符串
        2.2 创建空字符串
        2.3 判断字符串第1个元素是否为 ‘-’
            空字符串拼接 - 
        2.4 对传入的字符串反转
            去除 ‘0‘、’-’
            将结果拼接到空字符串中
        2.5 将其转为整型
        2.6 判断是否在 -2 ** 31 ~ 2 ** 31 -1
            返回转为整型的结果
        2.7 返回0
'''

def numberReverse(num: int) -> int:
    '''
        反转整数
    :param num: 整数
    :return: 反转后的整数结果
    '''
    if num == 0:
        return 0

    str_num = str(num)

    result = ''

    if str_num[0] == '-':
        result += '-'

    result += str_num[::-1].lstrip('0').rstrip('-')

    num = int(result)

    if -2 ** 31 < num < 2 ** 31 -1:
        return num

    return 0


print(numberReverse(123))
print(numberReverse(-123))
print(numberReverse(-12000000000))
print(numberReverse(0))