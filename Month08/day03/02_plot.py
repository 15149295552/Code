'''
最基本的绘图
'''
import numpy as np
import matplotlib.pyplot as plt

# x = np.array([1,2,3,4,5,6])
# y = np.array([14,7,9,5,3,11])
#
# plt.plot(x,y)
# plt.show()

# -π到+π的sin函数图像
# 将-π到+π拆分成200个点  np.linspace(起始值，终止值，个数)
xs = np.linspace(-np.pi,np.pi,200)

sinx = np.sin(xs)
plt.plot(xs,sinx,
         linestyle='--',
         linewidth=2,
         color='orangered',
         label=r'$y=sin(x)$')

cosx = np.cos(xs) / 2
plt.plot(xs,cosx,
         linestyle='-.',
         linewidth=5,
         color='dodgerblue',
         label=r'$y=\frac{1}{2}cos(x)$')

#设置坐标轴范围
# plt.xlim(0,np.pi+0.1)
# plt.ylim(0,1+0.1)

#设置坐标轴刻度   r'$latex表达式$'
plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
           [r'$-\pi$',r'$-\frac{\pi}{2}$',
            r'$0$',r'$\frac{\pi}{2}$',r'$\pi$'],
           fontsize=14,
           rotation=45) #旋转

plt.yticks([-1,-0.5,0,0.5,1],
           fontsize=14,
           rotation=45)

#设置坐标轴
ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data',0))
ax.spines['bottom'].set_position(('data',0))

plt.xticks(fontsize=14,rotation=45)
plt.yticks([-1,-0.5,0.5,1],fontsize=14,rotation=45)

#图例
plt.legend()

#特殊点
plt.scatter([np.pi/2,-np.pi/2],[1,-1],
            marker='*',
            s=400,
            edgecolors='red',
            facecolor='green',
            zorder=2)

plt.show()

