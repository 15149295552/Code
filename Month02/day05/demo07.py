"""
    列表推导式
        根据可迭代对象,以简易的方式构建新列表
        新列表 = [变量的操作 for 变量 in 可迭代对象 if 条件]
"""
# 需求1:将列表中大于10的元素存入新列表
list01 = [54,45,56,7,8,9,23]
# list_new = []
# for item in list01:
#     if item > 10:
#         list_new.append(item)
# print(list_new)

list_new = [item for item in list01 if item > 10]
print(list_new)


# 需求2:将列表中所有数字的个位存入新列表
# list_new = []
# for item in list01:
#     list_new.append(item % 10)
# print(list_new)

list_new = [item % 10 for item in list01]
print(list_new)















