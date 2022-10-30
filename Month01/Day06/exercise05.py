'''
练习：
    定义函数,根据小时、分钟、秒,计算总秒数

    调用：提供小时、分钟、秒
    调用：提供分钟、秒
    调用：提供小时、秒
    调用：提供分钟

    分析：
        1 定义函数：小时、分钟、秒都是缺省参数（通过调用分析）
        2 函数体：计算总秒数
            return 小时 * 3600 + 分钟 * 60 + 秒数
        3 调用
'''

def sum_seconds(hour=0, minute=0, second=0):
    '''
        计算总秒数
    :param hour: int，小时
    :param minute: int，分钟
    :param second: int，秒数
    :return: int，总秒数
    '''
    return hour * 3600 + minute * 60 + second

result = sum_seconds(1, 1, 1)
print(result)

print(sum_seconds(minute=2, second=3))
print(sum_seconds(hour=2, second=3))
print(sum_seconds(2, second=3))
print(sum_seconds(minute=2))