"""
    1. 根据列表中的数字,重复生成*.
        list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]
    效果：
        *
        **
        ***
        ****
        *****
        ****
        ***
        **
        *
"""
list01 = [1, 2, 3, 4, 5, 4, 3, 2, 1]

# 读取全部元素
for number in list01:
    print("*" * number) # 打印列表元素

# 修改全部元素
# for i in range(len(list01)):
#     print("*" * list01[i])

# 打印列表,通常测试
# print(list01)