# 创建字典存储香港信息、字典存储云南信息、字典存储广东信息
dict_hk = {'地区': '香港', '新增': 7, '现有': 171}
dict_yn = {'地区': '云南', '新增': 2, '现有': 68}
dict_gd = {'地区': '广东', '新增': 1, '现有': 40}

# 练习2：
# 在终端中打印香港的现有人数
print('香港的现有人数:', dict_hk['现有'])

# 在终端中打印云南的新增和现有人数
print('云南的现有人数:', dict_yn['现有'], '新增人数：', dict_yn['新增'])

# 广东新增人数增加1
dict_gd['新增'] += 1
print(dict_gd)

# 练习3：
# 删除香港现有人数信息
del dict_hk['现有']

# 删除广东新增人数信息
del dict_gd['新增']

# 删除云南的新增和现有信息
del dict_yn['新增']
del dict_yn['现有']

print(dict_hk, dict_gd, dict_yn)


# 练习4：
# 在终端中打印香港字典的所有键(一行一个)
# for k in dict_hk.keys():
#     print(k)

# 在终端中打印云南字典的所有值(一行一个)
# for v in dict_yn.values():
#     print(v)

# 在终端中打印广东字典的所有键和值(一行一个)
# for k, v in dict_gd.items():
#     print(k, v)

# 在广东字典中查找值是40对应的键名称
for k, v in dict_gd.items():
    if v == 40:
        print(k)