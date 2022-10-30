# 循环嵌套中的break语句

# for x in range(1, 4):
#     for y in range(1, 7, 2):
#         if y == 5:
#             break   # 终止内层循环（break语句在内层循环的循环体中）
#         print(y)
#     break   # 终止外层循环（break语句在外层循环的循环体中）
#     print('执行了break语句')   # 不执行


for x in range(1, 4):
    for y in range(1, 7, 2):   # 1 3 5
        if y == 5:
            continue   # 跳过本次内层循环
        print(y)
    continue   # 无意义