"""
    练习：定义数值累乘的函数
"""


# 由Python自动构建容器，存储需要计算的多个数据
def multiplicative(*args):  # (54,56,67,67,7,7,78)
    value = 1
    for item in args:
        value *= item
    return value


print(multiplicative(54, 56, 67, 67, 7, 7, 78))
print(multiplicative(54, 56, 67))

# def multiplicative(args):
#     value = 1
#     for item in args:
#         value *= item
#     return value
#
# # 由调用者自行构建容器，存储需要计算的多个数据
# print(multiplicative([54, 56, 67, 67, 7, 7, 78]))
# print(multiplicative((54, 56, 67)))
