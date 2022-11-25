'''
简单的基本绘图
'''
import numpy as np
import matplotlib.pyplot as plt

# x = np.array([1,2,3,4,5,6])
# y = np.array([14,7,18,11,19,8])
# plt.plot(x,y)
# plt.show()

#自定义窗口
plt.figure('test A',
           figsize=(10,8),
           facecolor='lightgray')

plt.title('Sin&Cos',fontsize=34)
plt.xlabel('X',fontsize=28)
plt.ylabel('Y',fontsize=28)
plt.grid(linestyle=':')


#绘制-π,+π的正弦,余弦函数图像
x = np.linspace(-np.pi,np.pi,200)
#sin
sinx = np.sin(x)
plt.plot(x,sinx,
         linestyle='--',
         linewidth=3,
         color='dodgerblue',
         label=r'$y=sin(x)$')
#cos
cosx = np.cos(x) / 2
plt.plot(x,cosx,
         linestyle='-.',
         linewidth=3,
         color='orangered',
         label=r'$y=\frac{1}{2}cos(x)$')

#设置坐标轴范围:第一象限
# plt.xlim(0,np.pi+0.1)
# plt.ylim(0,1+0.1)

#设置坐标轴刻度
# r'$latax表达式$'
# 分数:\frac{分子}{分母}   π: \pi

plt.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
           [r'$-\pi$',r'$-\frac{\pi}{2}$',r'$0$',
            r'$\frac{\pi}{2}$',r'$\pi$'],
           fontsize=18)

plt.yticks([-1,-0.5,0,0.5,1],
           fontsize=18)

#设置坐标轴,修改平面直角坐标系
ax = plt.gca()
ax.spines['bottom'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['right'].set_position(('data',0))
ax.spines['top'].set_position(('data',0))

plt.xticks(fontsize=18)
plt.yticks([-1,-0.5,0.5,1],fontsize=18)

#显示图例
plt.legend()

#特殊点
plt.scatter([np.pi/2,-np.pi/2],[1,-1],
            s=500, #点的大小
            marker='*',#点的形状
            edgecolors='red',#边缘颜色
            facecolor='green',#填充颜色
            zorder=3)#图层编号


plt.show()



