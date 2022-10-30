"""
    继承 - 数据
"""


class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age


# 子类没有构造函数,直接使用父类的
class Teacher(Person):
    pass


# 子类有构造函数,覆盖父类的(好像他不存在)
# 一定要用super函数调用父类构造函数
class Student(Person):
    # 子类构造函数参数：父类 + 自己
    def __init__(self, name="", age=0, score=0):
        super().__init__(name, age)
        self.score = score


xiao_pang = Student("下胖", 24, 88)
qtx = Teacher("祁大圣", 25)
print(xiao_pang.name)
