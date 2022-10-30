# 被导入的模块
name = 'python'


def func():
    '''
        测试模块中的test函数
    :return: None
    '''
    print('modu模块中的func函数')


class Animal:
    def eat(self):
        print('Animal类中eat方法')

    @classmethod
    def sleep(cls):
        print('Animal中的sleep方法')

if __name__ == '__main__':
    func()
    print(__name__)