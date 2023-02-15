'''
子图布局：矩阵式布局
'''
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure('Subplot',figsize=(8,6),
                 facecolor='lightgray')

# plt.subplot(3,3,5) #三行三列的第5副子图
# plt.plot([1,2,3],[1,2,3])
# plt.plot([1,2,3],[3,2,1])
# plt.xticks([])
# plt.yticks([])
#
# plt.subplot(3,3,1)
# plt.plot([1,2,3],[1,2,3])
# plt.plot([1,2,3],[3,2,1])
# plt.xticks([])
# plt.yticks([])

for i in range(1,10):
    plt.subplot(3,3,i)
    plt.text(0.5,0.5,i,fontsize=38,
             ha='center',va='center')
    plt.xticks([])
    plt.yticks([])

plt.tight_layout()

plt.show()




