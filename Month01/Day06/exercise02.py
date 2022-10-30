# 练习2：创建函数，在终端中打印矩形.
def print_star_rect(number):
    '''
        打印星星矩形
    :param number:int,边长
    :return: None
    '''
    for row in range(number):
        if row == 0 or row == number - 1:
            print("*" * number)
        else:
            print("*%s*" % (" " * (number - 2)))

number = int(input("请输入整数:"))  # 5
print_star_rect(number)

'''
    函数定义原则：
        函数功能明确，一个函数推荐完成一个特定的功能（功能单一）
'''