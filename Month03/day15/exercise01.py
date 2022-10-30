"""
请实现与02示例同样的功能，但是只写一个进程函数
"""
from multiprocessing import Process
from time import sleep
import os

def func(sec,info):
    sleep(sec)
    print(info)
    print(os.getppid(),"--",os.getpid())


# 循环创建子进程
data = [(4,"吃饭"),(2,"睡觉"),(3,"打豆豆")]
jobs = [] # 存储进程对象
for arg in data:
    p = Process(target=func,args=arg)
    jobs.append(p) #  存储对象
    p.start()

# 确保所有子进程结束
for i in jobs:
    i.join()

print("所有进程完成")



