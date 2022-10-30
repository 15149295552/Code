"""
    继承
        引入:
            财产:钱不用孩子挣,但是可以花
            编程:代码不用子类写,但是可以用

        适用性:
            多个类代码有共性,且概念统一
"""

"""
class Teacher:
    def say(self):
        print("说话")

    def teach(self):
        print("讲课")
 
class Student:
    def say(self):
        print("说话")

    def play(self):
        print("玩耍")
"""


class Person:
    def say(self):
        print("说话")


class Teacher(Person):
    def teach(self):
        self.say()
        print("讲课")


class Student(Person):
    def play(self):
        print("玩耍")


xiao_pang = Student()
xiao_pang.say()
xiao_pang.play()

shuang_er = Person()

# 关系判定
# -- 对象 是一种 类型
# isinstance(对象,类型  )
# 学生对象 是一种 学生类型
print(isinstance(xiao_pang, Student)) # True
# 学生对象 是一种 人类型
print(isinstance(xiao_pang, Person)) # True
# 人对象 是一种 学生类型
print(isinstance(shuang_er, Student)) # False

# -- 类型 是一种 类型
# issubclass(类型,类型)
# 学生类型 是一种 学生类型
print(issubclass(Student, Student)) # True
# 学生类型 是一种 人类型
print(issubclass(Student, Person)) # True
# 人类型 是一种 学生类型
print(issubclass(Person, Student)) # False

# -- 对象 是 类型
# print(type(对象) == 类型)
# 学生对象的类型 是 学生类型
print(type(xiao_pang) == Student) # True
# 学生对象的类型 是 人类型
print(type(xiao_pang) ==  Person) # False
# 人对象的类型 是 学生类型
print(type(shuang_er) == Student) # False
