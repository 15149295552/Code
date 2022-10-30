"""
    练习1：
    将两个列表，合并为一个字典
    姓名列表["张无忌","赵敏","周芷若"]
    房间列表[101,102,103]
    {101: '张无忌', 102: '赵敏', 103: '周芷若'}

    练习2：
    颠倒练习1字典键值
    {'张无忌': 101, '赵敏': 102, '周芷若': 103}
"""
list_name = ["张无忌", "赵敏", "周芷若"]
list_room = [101, 102, 103]

# dict_result = {}
# for i in range(len(list_name)):
#     key = list_name[i]
#     value = list_room[i]
#     dict_result[key] = value
# print(dict_result)

dict_result = {list_name[i]: list_room[i] for i in range(len(list_name))}
print(dict_result)

# new_dict = {}
# for k,v in dict_result.items():
#     new_dict[v] = k
# print(new_dict)

new_dict = {v: k for k, v in dict_result.items()}
print(new_dict)
