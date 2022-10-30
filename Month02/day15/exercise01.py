"""
    练习1：使用生成器表达式在列表中获取所有字符串.

    练习2：在列表中获取所有整数,并计算它的平方.
"""
list01 = [43, "a", 5, True, 6, 7, 89, 9, "b"]

# result = []
# for item in list01:
#     if type(item)  ==  str:
#         result.append(item)
# print(result)
# result = [item for item in list01 if type(item)  ==  str]

# 做
result = (item for item in list01 if type(item) == str)
# ...
# 用
for item in result:
    print(item)

# 练习2：在列表中获取所有整数,并计算它的平方.
result = (item ** 2 for item in list01 if type(item) == int)
for item in result:
    print(item)
