"""
    迭代自定义对象
"""


class StudentIterator: # 迭代器
    # 构造函数是一种创建对象的方式
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __next__(self):
        if self.index < len(self.data) - 1:
            self.index += 1
            return self.data[self.index]
        # 发送错误(通知结束循环)
        raise StopIteration()

class StudentController: # 可迭代对象
    def __init__(self):
        self.list_student = []

    def __iter__(self):
        return StudentIterator(self.list_student)


controller = StudentController()
controller.list_student.append("王淦")
controller.list_student.append("徐南晔")
controller.list_student.append("杨建宏")
# for item in controller:
#     print(item)
iterator = controller.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration: # 接收错误
        break
