'''
练习3：录入一个长字符串，打印每个字符及出现的次数。
效果：
    输入： java
    输出：
        字符 j 出现：1 次
        字符 a 出现：2 次
        字符 v 出现：1 次

分析：
    1 创建空字典 dict_data --> {字符:次数, ...}
    2 循环遍历字符串 --> 每个字符 char
        判断：字符是否在字典中
            不在：dict_data[char] = 1
            在：dict_data[char] += 1
    3 循环遍历字典
        按格式输出显示
'''

string = input('请输入字符串：')

dict_data = {}

for char in string:
    # 方法1
    if char not in dict_data:
        dict_data[char] = 1
    else:
        dict_data[char] += 1

    # 方法2：key唯一
    dict_data[char] = string.count(char)

for char, times in dict_data.items():
    print(f'字符{char} 出现：{times}次')
