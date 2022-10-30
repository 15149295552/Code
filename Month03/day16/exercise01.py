"""
练习：创建两个分支线程，一个用于打印1-52这52个数字
另一个用于打印 A-Z这26个字母。要求最终打印顺序为
12A34B56C .... 5152Z
"""
from threading import Thread,Lock

lock1 = Lock()
lock2 = Lock()

def print_num():
    for i in range(1,53,2):
        lock1.acquire()
        print(i)
        print(i+1)
        lock2.release()

def print_chr():
    for i in range(65,91):
        lock2.acquire()
        print(chr(i))
        lock1.release()

t1 = Thread(target=print_num)
t2 = Thread(target=print_chr)

lock2.acquire() #确保字母打印阻塞让数字先打印

t1.start()
t2.start()
t1.join()
t2.join()