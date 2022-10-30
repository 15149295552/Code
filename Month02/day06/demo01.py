"""
    字典基础操作
        创建
        添加
        定位(读取/修改)
        删除
        遍历
"""
# 列表：擅长于存储单一维度数据
list_name = ["马鹏", "王子依", "陆飞翔"]
list_sex = ["男", "女", "女"]
list_age = [27, 23, 25]

# 字典：擅长于存储多个维度数据
# 1. 创建
# -- 字典名 = {键1:值,键2:值}
dict_mp = {"name": "马鹏", "sex": "男", "age": 27}
dict_wzy = {"name": "王子依", "sex": "女", "age": 23}
dict_lfx = {"name": "陆飞翔", "sex": "女", "age": 25}

# -- 字典名 = dict(可迭代对象)
# 可迭代对象元素的要求:能够一分为二
list_name = ["马鹏", ("王", "子依"), ["陆", "飞翔"]]
dict_person = dict(list_name)
print(dict_person)

# 2. 添加
# 字典名[键] = 值
dict_mp["money"] = 10000000

# 3.定位
# --修改
# 字典名[键] = 值
dict_mp["sex"] = "女"
# --读取
# 字典名[键]
print(dict_mp["name"])
print(dict_mp)

# 4. 删除
# del 字典名[键]
del dict_mp["sex"]

# 5. 遍历
# -- for key in 字典:
for key in dict_wzy:
    print(key)

# -- for value in 字典.values():
for value in dict_wzy.values():
    print(value)

# item记录的是元组(键,值)
# for item in dict_wzy.items():
# -- for key,value in 字典.items():
for key, value in dict_wzy.items():
    print(key)
    print(value)

print(list(dict_lfx))  # ['name', 'sex', 'age']
print(list(dict_lfx.values()))  # ['陆飞翔', '女', 25]
print(list(dict_lfx.items()))  # [('name', '陆飞翔'), ('sex', '女'), ('age', 25)]
