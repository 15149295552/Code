"""
创建多个线程
"""
from threading import Thread
from time import sleep
import os


# 带有参数的线程函数
def func(name, sec):
    print(os.getpid(),"%s 线程开始啦" % name)
    sleep(sec)
    print("%s 线程结束哈哈哈哈" % name)


for i in range(5):
    t = Thread(target=func,
               args=("T-%d" % i,),
               kwargs={'sec': 2},
               daemon=True)
    t.start()
