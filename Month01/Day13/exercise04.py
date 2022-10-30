# 练习2：创建自定义range类，实现下列效果.

class RangeIterator(object):
    ''' 迭代器类 '''
    def __init__(self, end):
        self.__end = end
        self.__value = -1

    def __next__(self):
        self.__value += 1
        if self.__value == self.__end:
            raise StopIteration
        return self.__value

class MyRange:
    def __init__(self, stop):
        self.__stop = stop

    def __iter__(self):
        return RangeIterator(self.__stop)

for number in MyRange(5):
    print(number)  # 0 1 2 3 4