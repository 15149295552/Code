"""
同时创建多个子进程
"""
from multiprocessing import Process
from time import sleep
import os


def func01():
    sleep(4)
    print("吃饭")
    print(os.getppid(),"--",os.getpid())

def func02():
    sleep(2)
    print("睡觉")
    print(os.getppid(), "--", os.getpid())

def func03():
    sleep(3)
    print("打豆豆")
    print(os.getppid(), "--", os.getpid())

# 循环创建子进程
todo = [func01,func02,func03]
jobs = [] # 存储进程对象
for do in todo:
    p = Process(target=do)
    jobs.append(p) #  存储对象
    p.start()

# 确保所有子进程结束
for i in jobs:
    i.join()

print("所有进程完成")



