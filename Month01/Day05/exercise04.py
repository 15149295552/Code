'''
练习1：**列表转为字典**
    将两个列表，合并为一个字典
    姓名列表：["张无忌","赵敏","周芷若"]
    房间列表：[101,102,103]

        {101: '张无忌', 102: '赵敏', 103: '周芷若'}

分析：
    规律：两个列表的长度一致（list有序-->基于索引值进行索引，取到对应的元素）
    实现：
        1 创建空字典 dict_data
        2 循环列表的长度
        3 字典
            key: 房间列表[i]
            value:  姓名列表[i]
            {房间列表[i]: 姓名列表[i], ...}

            增加：
                dict_data[房间列表[i]] = 姓名列表[i]

'''

# 方法1
# list_name = ["张无忌", "赵敏", "周芷若"]
# list_room = [101, 102, 103]
#
# dict_data = {}
#
# for i in range(len(list_name)):
#     dict_data[list_room[i]] = list_name[i]
#
# print(dict_data)

# 方法2：列表长度不一致
list_name = ["张无忌", "赵敏", "周芷若"]
list_room = [101, 102, 103]

# 假设法
min_length = len(list_name)
if min_length > len(list_room):
    min_length = len(list_room)

dict_data = {}

for i in range(min_length):
    dict_data[list_room[i]] = list_name[i]

print(dict_data)