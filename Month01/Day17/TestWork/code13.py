'''
13、回文
  定义函数：根据传入的内容，判断是否会回文，是则提示是回文，否则提示不是回文。
    输入：'12321'
    输出：是回文

    输入：'自来水来自海上'
    输出：不是回文

  方法1：回文对称：正向与反向结果一致
     1 定义函数：plalindrome_check(string)
        1 判断字符串长度大于1
        2 判断： 正向字符串 与 反向字符串（反向切片） 对比
            是： 是回文
            否： 不是回文

  方法2：沿中心（基于索引值）判断
     1 定义函数：plalindrome_check(string)
        1 判断字符串长度大于1
        2 计算中心的索引值：len(string)//2
        3 遍历： range(len(string)//2) --> x
            if string[x] != string[len(string)-1-x]:
                print('不是回文')
                break
        4 else:
            print('是回文')
'''


# def plalindrome_check(string):
#     '''
#         判断字符串是否是回文
#     :param string: str，判断的字符串
#     :return: None
#     '''
#     if len(string) > 1:
#         if string == string[::-1]:
#             print(string, '是回文')
#         else:
#             print(string, '不是回文')

def plalindrome_check(string):
    '''
        判断字符串是否是回文
    :param string: str，判断的字符串
    :return: None
    '''
    if len(string) > 1:
        mid = len(string) // 2
        for x in range(mid):
            if string[x] != string[len(string) - 1 - x]:
                print(string, '不是回文')
                break
        else:
            print(string, '是回文')


plalindrome_check('1221')
plalindrome_check('上海自来水来自海上')
plalindrome_check('自来水来自海上')
