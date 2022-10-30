# 字典 dict

# # 表示
# # {key1:value1, key2:value2, ...}
#
# # 创建
# # 1 空字典
# d01 = {}
# d01 = dict()
# print(d01, type(d01))
#
# # 2 key:只能是不可变数据类型(value无限制数据类型)
# d02 = {2: 'two', 3.14: '圆周率', 'name': ['python', 'java'], (1, 3): 'tuple'}
# print(d02, type(d02))
# # d02 = {[3, 5]: 'list'}  # 字典的key是基于哈希计算，可变数据类型不能用于哈希运算
# # print(d02)
#
# # 3 key:唯一（不能重复）
# d03 = {'name': 'python', 'name': "java"}
# print(d03)
#
# # 4 字典存储无序
# d04 = {'name': 'python', 'year': 1991}
# d05 = {'year': 1991, 'name': 'python'}
# print(d04 == d05)
# print([1, 2, 3] == [3, 2, 1])
#
# # 5 构造函数：dict(可迭代对象)
# # d06 = dict(range(4))    # 不能创建字典
# # print(d06)
# d06 = dict([('name', 'python'), ('year', 1991)])
# d06 = dict((('name', 'python'), ('year', 1991)))
# d06 = dict(name='python', year=1991)
# print(d06)


# 查看
# dict01 = dict(language='python', creater='龟叔', year=1991)
# print(dict01)  # {'language': 'python', 'creater': '龟叔', 'year': 1991}
# print('长度：', len(dict01))
# print('存在：', 'python' in dict01)  # key in/not in dict
# print('索引：', dict01['creater'])   # dict[key]
# # print('索引：', dict01['creaters'])   # 注意：key 不存在，异常：KeyError
# print('索引：', dict01.get('creaters'))  # key 不存在，返回None
# print('所有key', dict01.keys(), list(dict01.keys()), 'year' in dict01.keys())
# print('所有value', dict01.values(), list(dict01.values()), 'python' in dict01.values())
# print('所有key和value', dict01.items())


# 增加/修改
# 语法：dict[key] = value
# dict02 = {'language': 'python', 'year': 1991}
# dict02['creater'] = '龟叔'   # 增加：键值对不存在
# print(dict02)
# dict02['creater'] = '吉多'   # 修改：键值对存在
# print(dict02)


# 删除
# dict03 = {'language': 'python', 'year': 1991, 'creater': '吉多'}
# result = dict03.pop('creater')
# print(result, dict03)
#
# del dict03['year']   # 常用
# print(dict03)


# 遍历
# dict04 = {'language': 'python', 'year': 1991, 'creater': '吉多'}

# 方法1：直接遍历 --> key
# for k in dict04:
#     print(k, dict04[k])

# 方法2：基于items方法
# print(dict04.items())
# for k, v in dict04.items():
#     print(k, v)


# 字典推导式
# # 需求：将1到10之间对应的数及平方存储到字典中 {1:1, 2:4, 3:9, .., 9:81}
# # 常规方法
# dict_data = {}
#
# for i in range(1, 10):
#     dict_data[i] = i ** 2
#
# print(dict_data)
#
# # 推导式
# print({i: i ** 2 for i in range(1, 10)})


# 需求：将1到10之间对应的偶数及平方存储到字典中 {2:4, 4:16, .., 8:64}
# 常规方法
dict_data = {}

for i in range(1, 10):
    if i % 2 == 0:
        dict_data[i] = i ** 2

print(dict_data)

# 推导式
print({i: i ** 2 for i in range(1, 10) if i % 2 == 0})
