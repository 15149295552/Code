"""
进程函数传参
"""
from multiprocessing import Process
from time import sleep

# 带有参数的进程函数
def worker(name,sec):
    for i in range(3):
        sleep(sec)
        print("I'm %s"%name)
        print("I'm working...")

# 按照位置传参
# p = Process(target=worker,args=("Tom",2))

# 关键字传参
p = Process(target=worker,
            args=("Tom",),
            kwargs={"sec":2},
            daemon=True) # 子进程会随着父进程结束而结束
p.start()

sleep(3)









