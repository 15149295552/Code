# 对象的判断函数

class Human:
    def say(self):
        print('hello')

class Student(Human):
    def study(self):
        print('学习使我快乐')

class Teacher(Human):
    def teach(self):
        print('教学是一种高尚的分享')

h01 = Human()
s01 = Student()
t01 = Teacher()

# 人对象 是一种 人类型
print(isinstance(h01, Human))
# 学生对象 是一种 人类型
print(isinstance(s01, Human))
# 老师对象 是一种 人类型
print(isinstance(t01, Human))
# 老师对象 是一种 学生类型
print(isinstance(t01, Student))


# 学生对象 不是 人类
print(type(s01) == Human)
# 人对象 是 人类
print(type(h01) == Human)

print(type(1) == int)