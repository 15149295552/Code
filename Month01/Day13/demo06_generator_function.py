# 内置生成器函数

# 需求: 将以下列表中元素打印: 排名及元素数据
# list_language = ['Python', 'C', 'Java', 'Php', 'C++']
#
# # 快捷输入: itere
# for code, lang in enumerate(list_language, 1):
#     # print(f'排名第:{code+1} 的编程语言是:{lang}')
#     print(f'排名第:{code} 的编程语言是:{lang}')

# 需求: 将以下列表按照位置组合
list_language = ['Python', 'C', 'Java', 'Php', 'C++']
list_code = [1, 3, 2, 6, 5, 7]

res = zip(list_language, list_code)
print(res)
for item in res:
    print(item)

print(dict(zip(list_language, list_code)))
print(dict(zip(list_language, list_code)).items())