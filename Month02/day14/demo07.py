"""
    内置生成器函数-zip
"""
list_name = ["张翠山", "周芷若", "张无忌"]
list_room = [101, 102, 103]
for item in zip(list_name, list_room):
    print(item)

# 容器(生成器)
print(list(zip(list_name, list_room)))
# [('张翠山', 101), ('周芷若', 102), ('张无忌', 103)]
print(dict(zip(list_name, list_room)))
# for i in range(len(list_name)):
#     key = list_name[i]
#     value = list_room[i]

list_map = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]
# 矩阵转置：列 -> 行
# new_map = []
# for item in zip(list_map[0], list_map[1], list_map[2],list_map[3]):
#     new_map.append(list(item))
# print(new_map)

# new_map = []
# for item in zip(*list_map):
#     new_map.append(list(item))
# print(new_map)
new_map = [list(item) for item in zip(*list_map)]
print(new_map)
# 练习：将两个列表合并为一个字典
# list_student_name = ["悟空", "八戒", "白骨精"]
# list_student_age = [28, 25, 36]