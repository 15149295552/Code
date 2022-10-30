"""
    重写:在子类定义与父类相同的方法。
        Person    object   __int__
                           __str__
                           __init__

        __str__函数每当打印对象时自动执行,
               用于定义对象呈现形式(print)
"""
class Person(object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 对象 --> 整整
    def __int__(self):
        return self.age

    # 对象 --> 字符串(没有限制)
    def __str__(self):
        return f"{self.name}的年龄{self.age}"

xiao_pang = Person("小胖", 23) # 内部:xiao_pang.__init__()
shuang_er = Person("双儿", 120)
print(xiao_pang) # 内部:xiao_pang.__str__()
print(shuang_er)
# print(str(xiao_pang))

print(int(xiao_pang)) # 内部:xiao_pang.__int__()
print(int(shuang_er))
