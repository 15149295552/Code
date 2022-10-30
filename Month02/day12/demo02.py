"""
   自定义对象浅拷贝
        __repr__函数每当调用repr时自动执行,
               用于对象浅拷贝(eval)
"""


class Person(object):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    # 对象 --> 字符串(python语法格式)
    def __repr__(self):
        return 'Person("%s", %s)' % (self.name, self.age)


xiao_pang = Person("小胖", 23)  # 内部:xiao_pang.__init__()
shuang_er = Person("双儿", 120)

# 类型转换:将字符串 作为 Python代码执行
# 结果 = eval(字符串)
# print(eval("1.2+1"))

# line = xiao_pang.__repr__() #存入到硬盘中
# # 从硬盘中读取字符串...
# obj = eval( line )
# print(obj.name)

# 浅拷贝
new = eval(xiao_pang.__repr__())
xiao_pang.name = "胖胖"
print(new.name)
