'''
填充图：满足条件，填充指定的颜色
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,8*np.pi,1000)
sin_y = np.sin(x)
cos_y = np.cos(x/2) / 2

fig = plt.figure('Fill',facecolor='lightgray')
plt.title('Fill',fontsize=20)
plt.xlabel('x',fontsize=14)
plt.ylabel('y',fontsize=14)
plt.grid(linestyle=':')

plt.plot(x,sin_y,color='dodgerblue',
         label=r'$y=sin(x)$')
plt.plot(x,cos_y,color='orangered',
         label=r'$y=\frac{1}{2}cos(\frac{x}{2})$')

#填充sin>cos部分
plt.fill_between(x,#x数据
                 sin_y,cos_y,#要比较的两个数据
                 sin_y>cos_y,#条件
                 color='dodgerblue',#满足条件的颜色
                 alpha=0.5)#透明度
#填充cos>sin的部分
plt.fill_between(x,#x数据
                 sin_y,cos_y,#要比较的两个数据
                 sin_y<cos_y,#条件
                 color='orangered',#满足条件的颜色
                 alpha=0.5)#透明度


plt.legend()
plt.show()




