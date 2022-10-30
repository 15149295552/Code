# 字符串 str

# 表示方式
# words = "This's a pen"
# print(words)
# words = 'This"s a pen'
# print(words)
#
# s1 = '''今天是星期三
# 还是很热的'''
# print(s1)
# s2 = """今天是星期三
# 还是很热的"""
# print(s2, type(s2))
# s3 = """'This"s a pen'"""
# print(s3)
# print(s3, 's3')


# 转义字符
# path = 'C:\tsers\tdministrator\nesktop\rIDVN2207'
# print(path)

# 进度条
# import time
#
# for i in range(1, 101):
#     print('\r{} {}%'.format('>' * i, i), end='')
#     time.sleep(0.1)

# 原始字符串(raw)   [重点]
# path = r'C:\tsers\tdministrator\nesktop\rIDVN2207'
# print(path)


# 格式字符串
# language = 'python'
# year = 1991
# rate = 12.789
# print('编程语言: ', language, ",发行年份: ", year, ",市场占有率为：", rate, '%', sep='')
#
# # 方法1：
# print('编程语言: %s,发行年份: %d,市场占有率为：%f%%' % (language, year, rate))
# print('编程语言: %s,发行年份: %d,市场占有率为：%.2f%%' % (language, year, rate))
# print('编程语言: %-10s,发行年份: %6d,市场占有率为：%8.2f%%' % (language, year, rate))
#
# # 方法2：
# print('编程语言: {},发行年份: {},市场占有率为：{}%'.format(language, year, rate))
# print('编程语言: {0},发行年份: {1},市场占有率为：{1}%'.format(language, year))
#
# # 方法3:
# print(f'编程语言: {language},发行年份: {year},市场占有率为：{rate}%')
#
# # 作用：生成一定格式的字符串
# base_path = 'https://bj.lianjia.com/ershoufang/pg%d/'
# for i in range(1, 11):
#     print(base_path % i)
#
# base_path = 'https://bj.lianjia.com/ershoufang/pg{}/'
# for i in range(1, 11):
#     print(base_path.format(i))
#
# for i in range(1, 11):
#     print(f'https://bj.lianjia.com/ershoufang/pg{i}/')


# 常用方法
# print(dir(str))
# print(help(str.join))

# 判断当前字符串中的所有字符全是数字  [重点]
print('123'.isdigit())
print('12.3'.isdigit())


# # 将字符（字母）转为全大写/小写
# print('Python'.upper())
# print('Python123'.upper())
# print('PyTHON123'.lower())
#
#
# # 去除指定字符 [重点]
# data = '  <p><a>images</a></p> \r\n '
# print(data.strip())  # 默认可以去：空格字符、\r \n
# data = '  <p><a>images</a></p>  '
# print(data.strip('<> pa/'))    # 去除字符
#
#
# # 字符替换 [重点]
# data = 'banana'
# print(data.replace('a', 'A'))   # 默认全部替换
# print(data.replace('a', 'A', 2))   # 指定替换个数
# print(data.replace('B', 'b'))   # 字符不存在，不替换
#
#
# # 统计字符出现的次数
# data = 'banana'
# print(data.count('a'))     # 统计a出现的次数
# print(data.count('a', 2))  # 从字符串索引值为2的位置向后统计a出现的次数
# print(data.count('a', 2, -2))