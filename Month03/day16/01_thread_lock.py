"""
线程锁演示
"""
from threading import Thread,Lock
from time import sleep

a = b = 1 # 共享资源
lock = Lock() # 锁对象

def value():
    while True:
        lock.acquire()
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release()

t = Thread(target=value)
t.start()

while True:
    lock.acquire() # 上锁
    a += 1
    sleep(0.0001)
    b += 1
    lock.release() # 解锁





