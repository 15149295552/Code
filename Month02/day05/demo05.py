"""
    列表 --> 字符串
        字符串 = "连接符".join(列表)
"""
# 多个元素 --连接--> 一个字符串
list01 = ["a", "b", "c"]
result = "-".join(list01)  # a-b-c
print(result)

# 应用
# 需求：根据需求循环拼接字符串
# 缺点：频繁修改不可变数据,每次都会产生垃圾
# result = ""
# for item in range(10):
#     # result += str(item)
#     # 每次循环产生一个新字符串
#     # 替换result中存储的地址
#     result = result + str(item)
# print(result)  # 0123456789

# 解决:使用可变数据代替不可变数据
result = []
for item in range(10):
    # 每次循环都向同一个列表添加
    result.append(str(item))
str_result = "".join(result)
print(str_result)
