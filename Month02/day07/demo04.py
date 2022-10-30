"""
    函数 - 返回值
    设计理念
        崇尚小而精,拒绝大而全
"""


# 需求:创建函数,实现两个数字相加
"""
def add():
    # 1. 获取数据
    one = int(input("请输入第一个数字:"))
    two = int(input("请输入第二个数字:"))
    # 2. 逻辑计算
    result = one + two
    # 3. 显示结果
    print("结果是:%s" % result)

add()
"""


def add(one,two):
    """
        实现两个数字相加
    :param one:数值类型,第一个数字
    :param two:数值类型,第二个数字
    :return:数值类型,相加的结果
    """
    result = one + two
    return result # 发送

# 接收
number = add(5,6)
print(number)