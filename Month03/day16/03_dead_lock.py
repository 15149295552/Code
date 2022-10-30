"""
死锁问题演示
"""
from threading import Thread,Lock
from time import sleep


class Bank:
    def __init__(self,id,balance,lock):
        self.id = id
        self.balance = balance # 余额
        self.lock = lock

    def get(self,num):
        self.balance -= num

    def put(self,num):
        self.balance += num

# obj1 --> obj2 转 num
def trans(obj1,obj2,num):
    obj1.lock.acquire()
    obj1.get(num)
    obj1.lock.release() # 不会死锁

    sleep(0.1)
    obj2.lock.acquire()
    obj2.put(num)

    # obj1.lock.release()
    obj2.lock.release()


if __name__ == '__main__':
    tom = Bank("tom",10000,Lock())
    abby = Bank("abby",8000,Lock())

    t1 = Thread(target=trans,args=(tom,abby,5000))
    t2 = Thread(target=trans,args=(abby,tom,5000))
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print("Tom:",tom.balance)
    print("Abby:",abby.balance)
