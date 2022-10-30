# 2、将列表中的元素按照长度分类并打印
#     language = ['Python', 'Java', 'C', 'R', 'C++', 'HTML', 'SQL']
#
#     输出：
#         长度为 6 的编程语言有：['Python']
#         长度为 4 的编程语言有：['java', 'HTML']
#         长度为 1 的编程语言有：['C', 'R']
#         长度为 3 的编程语言有：['C++', 'SQL']

'''
    存储结构：{长度值: [编程语言1, 编程语言2, ...]}

    1 定义空字典 dict_lang
    2 循环遍历列表  --> 每门编程语言
        1 计算编程语言字符串的长度值
        2 判断
            不存在
                dict_lang[长度值] = [编程语言]
            存在
                dict_lang[长度值].append(编程语言)
        3 循环打印
'''
# 方法1
# language = ['Python', 'Java', 'C', 'R', 'C++', 'HTML', 'SQL']
#
# dict_lang = {}
#
# for lang in language:
#     length = len(lang)
#     if length not in dict_lang:
#         dict_lang[length] = [lang]
#     else:
#         dict_lang[length].append(lang)
#
# print(dict_lang)
#
# for len, lang in dict_lang.items():
#     print(f'长度为:{len} 的编程语言有：{lang}')


# 方法2
language = ['Python', 'Java', 'C', 'R', 'C++', 'HTML', 'SQL']

dict_lang = {}

for lang in language:
    length = len(lang)
    if length not in dict_lang:
        dict_lang[length] = []
    dict_lang[length].append(lang)

print(dict_lang)

for len, lang in dict_lang.items():
    print(f'长度为:{len} 的编程语言有：{lang}')