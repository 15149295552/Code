'''
4. 输出单词频率编写一个程序来计算输入中单词的频率。 按字母顺序对键进行排序后输出。
'''

'''
分析：
    1 创建字典：{单词：出现的次数, ...}
    2 遍历每个单词：输入的字符串内容按空格分割
    3 排序：基于key使用sorted排序
    4 打印：遍历字典的key与value
'''


def wordFreq(content: str):
    '''
        计算并打印单词及单词出现的次数
    :param content: 字符串数据
    :return: None
    '''
    freq = {}

    for word in content.split():
        freq[word] = freq.get(word, 0) + 1

    list_words = sorted(freq.keys())

    for word in list_words:
        print(f"{word}:{freq[word]}")

wordFreq('this is a pen, this is a book')
