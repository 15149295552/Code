"""
练习： 有500张票，分别记为 T1---T500,存入列表
有10个线程模拟10个售票窗口记为W1--W10，
各自买票互不影响。
每卖出一张票 打印一下 “W1 -- T250”,暂停0.1秒表示
出票时间。直到所有票卖完打印一句 “票已售罄”
"""
from threading import Thread
from time import sleep

tickets = ["T%d" % i for i in range(1, 501)]


# 卖票
def sell(win):
    while tickets:
        print("%s -- %s"%(win,tickets.pop(0)))
        sleep(0.1)


jobs = []
for i in range(1, 11):
    t = Thread(target=sell, args=("W%d" % i,))
    jobs.append(t)
    t.start()

# 判断是否所有线程都结束
for i in jobs:
    i.join()
print("票已售罄")
