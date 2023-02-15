'''
散点图
'''
import numpy as np
import matplotlib.pyplot as plt

height = np.random.normal(175,5,2000)
weight = np.random.normal(70,5,2000)

plt.scatter(height,weight,c=height,cmap='jet')
plt.colorbar()

plt.show()







