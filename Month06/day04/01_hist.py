'''
直方图
'''
import numpy as np
import matplotlib.pyplot as plt


data = np.random.normal(175,5,10000)


plt.hist(data,bins=100)

plt.show()


