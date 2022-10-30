"""
    列表
        优点:支持索引/切片,可以修改,可以反复使用
        缺点:占用内存较多

    生成器
        优点:几乎不占内存
        缺点:不支持索引/切片
            不能修改数据
            只能使用一次
        适用性:优先
        解决:list(生成器)

    结论：
        函数返回多个结果使用yield
        函数返回单个结果使用return
        如果遇到生成器的缺点,转换为容器即可
"""
list_data = [1.6, 1.5, 88]

def find_all_float():
    for item in list_data:
        if type(item) == float:
            yield item

result = find_all_float()
# print(result[2])
# 生成器不能重复使用
a = result.__iter__() # 返回自身对象
b = result.__iter__() # 返回自身对象
print(a)
print(b)
for item in result:
    print(item)
for item in result:
    print(item)

# 列表可以重复使用
list01 = [10,20]
a = list01.__iter__() # 创建新迭代器
print(a)
b = list01.__iter__() # 创建新迭代器
print(b)

for item in list01:
    print(item)
for item in list01:
    print(item)




find_all_float = (item for item in list_data if type(item) == float)