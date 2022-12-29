'''
3.实现 strStr() 函数
  给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回 -1 。
'''

def strStr(haystack: str, needle: str) -> int:
    '''
        查找子字符串在字符串中的索引值位置
    :param haystack: 字符串
    :param needle: 子字符串
    :return: 索引值
    '''
    # 1 子字符串长度大于字符串的长度，直接返回-1
    if len(needle) > len(haystack):
        return -1

    # 2 使用切片：基于字符串的长度比较
    i = 0
    length = len(needle)
    while i + length <= len(haystack):
        if haystack[i: i + length] == needle:
            return i
        i += 1

    return -1


print(strStr('hello', 'll'))
print(strStr('aaaaa', 'bba'))
print(strStr('', ''))



