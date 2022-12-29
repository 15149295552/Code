'''
6.串联所有单词的子串
  给定一个字符串 s 和一些 长度相同 的单词 words 。找出 s 中恰好可以由 words中所有单词串联形成的子串的起始位置。注意子串要与 words 中的单词完全匹配，中间不能有其他字符 ，但不需要考虑 words 中单词串联的顺序。
'''
from typing import List

'''
分析
  1 创建列表：存储words组合出现在字符串中的索引值位置
  2 计算数据：字符串长度、words列表长度、列表元素长度、取值的长度（单词个数 * 单词长度）、计算words中每个单词的次数
  3 循环：字符串长度 - 取值的长度 + 1 --> i
    3.1 创建空计数器：Counter
    3.2 循环：range(i, i + 取值的长度, 单词长度） --> j
        3.2.1 长字符串[j:j+单词长度]
        3.2.2 计数：单词：+1
    
    3.3 判断 内部计数 是否与 计算words中每个单词的次数 相等：
        3.3.1 列表中存储 i 
  4 返回存储位置的列表
  
  s = "barfoothefoobarman", words = ["foo","bar"]
    
'''

from collections import Counter


def findSubstring(string: str, words: List[str]) -> List[int]:
    '''
        查找串联所有单词的子串的索引值位置
    :param string: 字符串
    :param words: 存储子字符串的列表
    :return: 存储字符串位置的索引列表
    '''
    list_loc = []  # 存储字符串位置的索引
    len_string = len(string)  # 字符串的长度
    number_word = len(words)  # 存储子字符串列表的长度
    len_word = len(words[0])  # 子字符串的长度
    window_size = number_word * len_word  # 滑动窗口的长度
    pattern = Counter(words)  # 子字符串的计数器

    for i in range(len_string - window_size + 1):
        counter = Counter()  # 空计数器
        for j in range(i, i + window_size, len_word):  # 每间隔单词长度取字符串
            sub_str = string[j: j + len_word]
            counter[sub_str] += 1

        if counter == pattern:  # 内部计数器是否等于words计数器
            list_loc.append(i)

    return list_loc


print(findSubstring("barfoothefoobarman",
                    words=["foo", "bar"]))
print(findSubstring("wordgoodgoodgoodbestword",
                    words=["word", "good", "best", "word"]))
print(findSubstring("barfoofoobarthefoobarman",
                    words=["bar", "foo", "the"]))
