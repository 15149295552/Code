'''
8、斐波那契数列
    定义函数：输入一个大于1的个数，计算其区间内指定个数的斐波那契数列存储至列表中，并打印出结果。
    斐波那契数列： 从第3个数开始，后一个数等于前两个数之和。
       1 1 2 3 5 8 13 ...   (产兔子)

分析:
    方案1: 序列赋值
        1 定义函数: fbnq(count)
        2 判断count > 1
            1 创建列表
            2 定义变量: a, b = 0, 1
            3 循环range(count)
                1 序列赋值: a, b = a+b, a
                2 将a添加至列表
        3 返回列表

    方案2: 列表
        1 定义函数: fbnq(count)
        2 判断count > 1
            1 创建列表=[1, 1]
            2 循环 range(count-2)
                列表.append(列表[-1] + 列表[-2])
        3 返回列表

    方案3: 递归函数
        1 定义函数: fbnq(count) --> 计算递归的结果
        2 定义结束条件: count <= 2  return 1
          return fbnq(count-1) + fbnq(count-2)
        3 创建列表
        4 循环 range(count)
           调用函数存储斐波那契数列
'''


# 方法1: 序列赋值
# def fbnq(count):
#     '''
#         计算并返回指定个数的斐波那契数列
#     :param count: int,个数
#     :return: list,存储斐波那契数列的列表
#     '''
#     if count > 1:
#         a, b = 0, 1
#         list_fbnq = []
#         for i in range(count):
#             a, b = a + b, a
#             list_fbnq.append(a)
#         return list_fbnq
#
#
# print(fbnq(5))


# 方法2: 列表
# def fbnq(count):
#     '''
#         计算并返回指定个数的斐波那契数列
#     :param count: int,个数
#     :return: list,存储斐波那契数列的列表
#     '''
#     if count > 1:
#         list_fbnq = [1, 1]
#         for i in range(count-2):
#             number = list_fbnq[-1] + list_fbnq[-2]    # 第三个数等于列表中后2个元素之和
#             list_fbnq.append(number)
#         return list_fbnq
#
# print(fbnq(50))


# 方法3: 递归函数
def fbnq(count):
    '''
        计算指定个数对应的斐波那契数列值
    :param count: int,个数
    :return: 对应的斐波那契数列值
    '''
    if count <= 2:
        return 1
    return fbnq(count-1) + fbnq(count-2)

list_fbnq = []
for i in range(1, 6):
    list_fbnq.append(fbnq(i))

print(list_fbnq)








