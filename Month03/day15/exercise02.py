"""
练习：
求100000以内的质数之和
1. 使用单个函数求值，获取函数执行时间 -》单进程
2. 请使用4个进程，完成同样的任务，同样统计用时
"""
import time
from multiprocessing import Process,Queue

q = Queue()

# 判断一个数是否为质数
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True

def prime_sum(begin,end):
    prime = [] # 存质数
    for i in range(begin,end):
        if is_prime(i):
            prime.append(i)
    q.put(sum(prime))


def get_result():
    for i in range(1,100001,5000):
        p = Process(target=prime_sum,args=(i,i+5000))
        p.start()

    res = 0
    for i in range(20):
        res += q.get()
    print(res)

begin = time.time()
get_result()  # 用时： 6.55269718170166
print("用时：",time.time() - begin)



# def process_1():
#     prime = [] # 存质数
#     for i in range(1,100001):
#         if is_prime(i):
#             prime.append(i)
#     print(sum(prime))
#
# begin = time.time()
# process_1() # 用时： 12.914330005645752
# print("用时：",time.time() - begin)