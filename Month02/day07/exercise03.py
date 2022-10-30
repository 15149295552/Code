"""
    练习1： 定义函数,在终端中打印一维列表.
    list01 = [5, 546, 6, 56, 76, ]
    for item in list01:
        print(item)

    list02 = [7,6,879,9,909,]
    for item in list02:
        print(item)
"""


# -----------定义函数-----------------
def print_list(list_target):  # 2  4
    for item in list_target:
        print(item)

# -----------使用函数-----------------
list01 = [5, 546, 6, 56, 76, ]
list02 = [7, 6, 879, 9, 909, ]
# 调试按F7进入函数
print_list(list01)  # 1