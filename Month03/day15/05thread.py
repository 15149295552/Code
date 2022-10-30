"""
创建一个基本的线程
"""
from threading import Thread
from time import sleep


a = 1

# 写一个线程函数
def func():
    for i in range(3):
        sleep(2)
        print("我是一个线程啊")
    global a
    print("a =",a)
    a = 10000

# 实例化线程对象
t = Thread(target=func)
t.start() # 启动线程

for i in range(4):
    sleep(1)
    print("我是主线程啊")

t.join()  # 阻塞等待分支线程结束
print("a :",a) # 10000