"""
进程间通信
"""
from multiprocessing import Process,Queue

# 创建消息队列
q = Queue()

# 进程函数
def handle():
    opt = q.get() # 从消息队里取内容
    if opt == "+":
        print("加法运算")
    elif opt == '-':
        print("减法运算")

p = Process(target=handle)
p.start()

opt = input("符号:")
q.put(opt) # 存入消息
