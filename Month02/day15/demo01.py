"""
    生成器表达式
        根据可迭代对象,以简易的方式构建新列表

"""
# 需求1:将列表中大于10的元素存入新列表
list01 = [54, 45, 56, 7, 8, 9, 23]
list_new = [item for item in list01 if item > 10]
for item in list_new:
    print(item)

generator_new = (item for item in list01 if item > 10)
for item in generator_new:
    print(item)

# 需求2:将列表中所有数字的个位存入新列表
list_new = [item % 10 for item in list01]
for item in list_new:
    print(item)
generator_new = (item % 10 for item in list01)
for item in generator_new:
    print(item)
