"""
    专业术语
        全局变量：定义在文件中,全文件可用
        函数：对很多代码打包,提高代码复用性与可读性
        局部变量：定义在函数中,一个函数内部可用

        类：抽象的概念,指类别,连接现实与虚拟的桥梁
            类与类行为不同
        对变量：对象名词性的修饰
        实例方法象：具体的实例,指个体,在虚拟中与现实对应
        实例:对象动词性的行为

    实例成员
        实例变量:在__init__中,通过对象创建
                在任意位置,通过对象访问
                表达不同个体的不同信息
        实例方法:操作实例变量

"""
# 全局变量只有1个,只能操作1个数据
name = "小胖"
name = "小红"
# 实例变量每个对象都有一个

class Wife:
    def __init__(self, name=""):
        # 创建实例变量：对象名.名称
        self.name = name

    def work(self):
        print(self.name, "在工作")


jian_ning = Wife("建宁")
# 读取实例变量：对象名.名称
print(jian_ning.name)
# 打印自定义对象
# <__main__.Wife object at 0x7f925914c7c0>
print(jian_ning)
# 自定义对象的内置实例变量__dict__：存储对象所有实例变量
# {'name': '建宁'}
print(jian_ning.__dict__)

# 调用实例方法：对象名.名称()
jian_ning.work()

# 不建议在类外创建实例成员
# class Wife:
#     pass
#
# w = Wife()
# # 对象.名称
# w.name = "建宁"
# print(w.name) # 建宁

# 不建议在__init__外创建实例变量
"""
class Wife:
    def set_name(self,name):
        self.name = name

w = Wife()
w.set_name("建宁")
print(w.name) # 建宁
"""
