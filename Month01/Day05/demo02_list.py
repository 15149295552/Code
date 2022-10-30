# 列表推导式

# 用法1：
# 需求：将1-10之间所有数的平方存储在列表中
# 常规方法
# list_data = []
#
# for i in range(1,10):
#     list_data.append(i**2)
# print(list_data)
#
# # 推导式
# print([i ** 2 for i in range(1, 10)])


# 用法2：
# 需求：将1-10之间偶数的平方存储在列表中
# 常规方法
# list_data = []
#
# for i in range(1, 10):
#     if i % 2 == 0:
#         list_data.append(i**2)
# print(list_data)
#
# # 推导式
# print([i**2 for i in range(1, 10) if i % 2 == 0])


# 方法3
list_color = ['♥', '♦', '♣', '♠']
list_char = ['A', 'J', 'Q', 'K']

# 常规方法
list_packer = []

for c in list_color:
    if c != '♠':
        for char in list_char:
            if char == 'K':
                list_packer.append(c+char)
print(list_packer)

# 推导式
print([c+char for c in list_color if c != '♠' for char in list_char if char == 'K'])