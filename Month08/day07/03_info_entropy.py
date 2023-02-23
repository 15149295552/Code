'''
信息熵计算演示
'''
import math
import matplotlib.pyplot as plt
import numpy as np


def cal_entropy(n):
    p = 1.0 / n
    total_entropy = 0.0

    for i in range(n):
        pi = p * math.log2(p)
        total_entropy += pi
    return -total_entropy

ret = []
for i in range(1,11):
    entropy = cal_entropy(i)
    ret.append(entropy)
    
plt.plot(np.arange(1,11),ret,'o-')
plt.show()
