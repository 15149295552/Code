"""
    私有成员:以双下划线命名(不以双下划线结尾)
        --实例变量
        --实例方法
        本质：自动修改私有变量名
            改为：单下划线+类名+私有变量名
        目的：类外无法访问
"""


class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        self.__age = age

    def __take_bath(self):
        print("在洗澡")

    def work(self):
        self.__take_bath()
        print("工作")

shuang_er = Wife("双儿", 26)
print(shuang_er.name)
# shuang_er.__take_bath()
# print(shuang_er.__age)
print(shuang_er.__dict__)
# print(shuang_er._Wife__age) # 不建议
shuang_er.work()