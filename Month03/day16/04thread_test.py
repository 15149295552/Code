"""
求100000以内的质数之和
线程
"""
import time
from threading import Thread

res = 0

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
    global res
    res += sum(prime)


def get_result():
    jobs = []
    for i in range(1,100001,10000):
        t = Thread(target=prime_sum,args=(i,i+10000))
        jobs.append(t)
        t.start()

    for i in jobs:
        i.join()

    print(res)

begin = time.time()
get_result()  # 用时： 12.95675802230835
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