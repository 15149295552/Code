"""
    迭代器 -> yield
"""
class StudentController: # 可迭代对象
    def __init__(self):
        self.list_student = []

    def __iter__(self):
        # 自动产生迭代器代码的大致规则:
        # -- 将yield以前的代码定义在__next__函数中
        # -- 将yield以后的数据作为__next__函数返回值
        index = 0
        yield self.list_student[index]

        index += 1
        yield self.list_student[index]

        index += 1
        yield self.list_student[index]


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
