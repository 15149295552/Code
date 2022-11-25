'''
散点图
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(175,5,500)
y = np.random.normal(60,5,500)

plt.scatter(x,y,
            s=75,
            c=x,
            cmap='jet')

plt.colorbar()#颜色条


plt.show()






