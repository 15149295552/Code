"""
    练习3：根据下列代码，创建降序排列函数。
    list01 = [5, 15, 25, 35, 1, 2]
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            if list01[r] < list01[c]:
                list01[r], list01[c] = list01[c], list01[r]
    print(list01)
"""
# 函数内部修改传入的可变对象
"""
def descending_order(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] < list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]
    return list_target

list01 = [5, 15, 25, 35, 1, 2]
new_list = descending_order(list01)
print(new_list) 
"""

def descending_order(list_target):
    for r in range(len(list_target) - 1):
        for c in range(r + 1, len(list_target)):
            if list_target[r] < list_target[c]:
                list_target[r], list_target[c] = list_target[c], list_target[r]

list01 = [5, 15, 25, 35, 1, 2]
descending_order(list01)
# 没有返回值,而是通过传入的列表,查看结果
print(list01)

