"""
上锁解决方案
"""
from threading import Thread,Lock
from time import sleep

lock = Lock()

tickets = ["T%d" % i for i in range(1, 501)]

# 卖票
def sell(win):

    while True:
        sleep(0.1)
        lock.acquire()
        if tickets:
            print("%s -- %s"%(win,tickets.pop(0)))
            lock.release()
        else:
            lock.release()
            break


jobs = []
for i in range(1, 11):
    t = Thread(target=sell, args=("W%d" % i,))
    jobs.append(t)
    t.start()

# 判断是否所有线程都结束
for i in jobs:
    i.join()
print("票已售罄")
