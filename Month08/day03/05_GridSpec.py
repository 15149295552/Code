'''
子图：网格式布局
'''
import matplotlib.pyplot as plt

gs = plt.GridSpec(3,3)

plt.subplot(gs[0,:2])
plt.text(0.5,0.5,'Python_Base',fontsize=28,
         ha='center',va='center')
plt.xticks([])
plt.yticks([])

plt.subplot(gs[:2,-1])
plt.text(0.5,0.5,'Socket',fontsize=28,
         ha='center',va='center')
plt.xticks([])
plt.yticks([])

plt.subplot(gs[-1,-2:])
plt.text(0.5,0.5,'Dashop',fontsize=28,
         ha='center',va='center')
plt.xticks([])
plt.yticks([])

plt.subplot(gs[-2:,0])
plt.text(0.5,0.5,'AI',fontsize=28,
         ha='center',va='center')
plt.xticks([])
plt.yticks([])

plt.subplot(gs[1,1])
plt.text(0.5,0.5,'2210',fontsize=28,
         ha='center',va='center')
plt.xticks([])
plt.yticks([])

plt.show()




