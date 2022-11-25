'''
子图:矩阵式布局
'''
import numpy as np
import matplotlib.pyplot as plt

plt.figure('subplot',figsize=(10,8),facecolor='lightgray')

# for i in range(1,10):
#     plt.subplot(3,3,i) #3行3列的第五幅子图
#     plt.plot([1,2,3],[1,2,3])
#     plt.plot([1,2,3],[3,2,1])
#     plt.xticks([])
#     plt.yticks([])

for i in range(1,10):
    plt.subplot(3,3,i)
    plt.text(0.5,0.5,#x,y的坐标
             i,#文本内容
             fontsize=98,#字体大小
             ha='center',#水平:left,center,right
             va='center')#垂直:top center, bottom
    plt.xticks([])
    plt.yticks([])

plt.tight_layout()




plt.show()
