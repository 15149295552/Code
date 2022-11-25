'''
子图布局:网格式布局,可以合并相邻的子图
'''

import numpy as np
import matplotlib.pyplot as plt

plt.figure('GridSpec',figsize=(10,8),facecolor='lightgray')

#三行三列的网格对象
gs = plt.GridSpec(3,3)

plt.subplot(gs[0,:2])
plt.text(0.5,0.5,'python_base',
         fontsize=50,
         ha='center',
         va='center')
plt.xticks([])
plt.yticks([])

plt.subplot(gs[:2,-1])
plt.text(0.5,0.5,'Socket',
         fontsize=50,
         ha='center',
         va='center')
plt.xticks([])
plt.yticks([])

plt.subplot(gs[-1,-2:])
plt.text(0.5,0.5,'dadashop',
         fontsize=50,
         ha='center',
         va='center')
plt.xticks([])
plt.yticks([])

plt.subplot(gs[-2:,0])
plt.text(0.5,0.5,'AI',
         fontsize=50,
         ha='center',
         va='center')
plt.xticks([])
plt.yticks([])

plt.subplot(gs[1,1])
plt.text(0.5,0.5,'AID2208',
         fontsize=50,
         ha='center',
         va='center')
plt.xticks([])
plt.yticks([])

plt.show()




