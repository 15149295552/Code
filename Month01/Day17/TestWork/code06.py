'''
6、鉴别关键字
    定义类：判断传入的关键字（str 类型），是否符合Python变量规范。
    符合规范，则打印关键字：xxx 合法，否则打印：xxx 不合法。
    规范：
        1、只能由数字、字母、下划线组成。
        2、数字不能开头。
        3、不能使用Python关键字。
        4、不能与内置函数名同名。

分析:
    1 定义类: StringCheck
    2 构造方法:
        keyword
        4个方法:
            1 判断字符串是否有其他字符(数字、字母、下划线) -- 私有化
                返回值: bool
            2 判断数字不能开头(索引字符串的第1个元素) -- 私有化
                返回值: bool
            3 判断字符串是否使用Python关键字 -- 私有化
                返回值: bool
            4 判断字符串是否与内置函数名同名 -- 私有化
                返回值: bool
            5 定义主方法,提供给用户调用 --> 接口
    3 实例化对象,调用对应的方法
'''

import string
import keyword

class StringCheck:
    def __init__(self, kword):
        self.keyword = kword
        self.__number = string.digits
        self.__chars = self.__number + string.ascii_letters + '_'

    def __is_group_sure(self):
        '''
            判断字符串中是否有其他的字符
        :return: bool,存在返回False,否则返回True
        '''
        for char in self.keyword:
            if char not in self.__chars:   # 有特殊字符,则返回False
                return False
        return True

    def __is_number_start(self):
        '''
            判断是否是数字开头
        :return: bool,是返回False,否则返回True
        '''
        if self.keyword[0] in self.__number:
            return False
        return True

    def __is_python_keyword(self):
        '''
            判断是否是python关键字
        :return: bool,是返回False,否则返回True
        '''
        if self.keyword in keyword.kwlist:   # 如果在python关键字列表中,返回False
            return False
        return True

    def __is_python_function(self):
        '''
            判断是否是python内置函数
        :return: bool,是返回False,否则返回True
        '''
        if self.keyword in dir(__builtins__):  # 如果在python内置函数列表中,返回False
            return False
        return True

    def string_check(self):
        if len(self.keyword) > 0:
            if self.__is_group_sure() and \
                self.__is_number_start() and \
                    self.__is_python_keyword() and \
                    self.__is_python_function():
                print(self.keyword, '合法')
            else:
                print(self.keyword, '不合法')
        else:
            print('字符串不能为空')

if __name__ == '__main__':
    check = StringCheck('')
    check.string_check()