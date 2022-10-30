"""
自定义线程类
"""
from threading import Thread

class MyThread(Thread):
    def __init__(self,value):
        self.value = value
        super().__init__()

    def run(self):
        for i in range(self.value):
            print("自定义的线程类")

t = MyThread(3)
t.start() # 创建线程自动执行run