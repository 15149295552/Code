"""
    练习1：以面向对象思想,描述下列情景.
    小明请保洁打扫卫生
"""


# 方式1:直接创建对象（每次都使用新的）
class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self):
        print("通知保洁")
        cleaner = Cleaner()
        cleaner.cleaning()


class Cleaner:
    def cleaning(self):
        print("打扫卫生")


xm = Client("小明")
xm.notify()

# 方式2:构造函数中创建对象（每次都使用一个）
"""
class Client:
    def __init__(self, name=""):
        self.name = name 
        self.cleaner = Cleaner()

    def notify(self):
        print("通知保洁")
        self.cleaner.cleaning()

class Cleaner:
    def cleaning(self):
        print("打扫卫生")

xm = Client("小明") # 创建保洁对象
xm.notify()
xm.notify()
"""

# 方式3:通过参数传递对象（最灵活）
"""
class Client:
    def __init__(self, name=""):
        self.name = name

    def notify(self, server):
        print("通知保洁")
        server.cleaning()
 
class Cleaner:
    def cleaning(self):
        print("打扫卫生")
 
xm = Client("小明")
cleaner = Cleaner()
xm.notify(cleaner)
"""
