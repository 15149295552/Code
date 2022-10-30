# 语句

# 3个物理行，3个逻辑行
# a = 10
# b = 20
# print(a, b)

# a = 10; b = 20    # 不推荐
# print(a, b)
#
# # a = 10
# # b = 20  # 不推荐
# # print(a, b)
#
# # 物理行长 --》换行
# print(1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)
#
# # 显式换行
# # \  续行符，表示下一行也是上一行未完的语句
# result = 1 + 2 + \
#          3 + 4 + \
#          5 + 6 + \
#          7 + 8
# print(result)
#
# # 隐式换行
# result = (1 + 2 +
#           3 + 4 +
#           5 + 6 +
#           7 + 8)
# print(result)
# def func(num):
#     for i in range(num):
#         if i > 4:
#             return
#         print(i, end='')
#
#
# func(6)
name = "张无忌"
names = ["赵敏", "周芷若"]
tuple01 = ("张翠山", name, names)
name = "无忌哥哥"
tuple01[2][0] = "敏儿"
print(tuple01)
