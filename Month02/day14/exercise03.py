"""
    练习2：创建自定义range类，实现下列效果.
"""


class MyRangeIterator:
    def __init__(self, stop):
        self.number = -1
        self.stop = stop

    def __next__(self):
        if self.number < self.stop - 1:
            self.number += 1
            return self.number
        raise StopIteration()


class MyRange:
    def __init__(self, end):
        self.end = end

    def __iter__(self):
        return MyRangeIterator(self.end)


# for number in MyRange(5):
#     print(number)# 0 1 2 3 4
obj = MyRange(5)
iterator = obj.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)  # 0 1 2 3 4
    except StopIteration:
        break
