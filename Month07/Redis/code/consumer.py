"""
    消费者
"""
import redis
from threading import Thread

r = redis.Redis()


def func():
    while True:
        # task: (b"tasks_list", b"task01")
        task = r.brpop("tasks_list", 0)
        print("正在执行任务:", task[1].decode())


t_list = []
for i in range(5):
    t = Thread(target=func)
    t.start()

for t in t_list:
    t.join()







