"""
创建一个进程
"""
from multiprocessing import Process
from time import sleep

a = 1  # 全局变量

# 创建进程函数
def func():
    print("开始一个任务")
    sleep(3) # 模拟一个任务的执行时间
    print("我的任务完成啦")
    global a
    print("a =",a) # 能使用
    a = 10000


# 实例化进程对象
p = Process(target=func)
p.start() # 启动进程

print("哈哈哈 我也干活啦")
sleep(4)
print("哈哈哈 我也干完啦")

# 阻塞等待子进程结束
p.join()
print("a :",a) # ?









