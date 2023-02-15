'''测试窗口，以及窗口的常见参数'''
import numpy as np
import matplotlib.pyplot as plt

fig1 = plt.figure('Test A',figsize=(8,6),
                  facecolor='lightgray')

xs = np.linspace(-np.pi,np.pi,200)
sinx = np.sin(xs)
plt.plot(xs,sinx,
         linewidth=3,
         color='orangered')

plt.title('哈哈哈',fontsize=28)
plt.xlabel('X',fontsize=20)
plt.ylabel('Y',fontsize=20)
plt.grid(linestyle=':')
plt.tight_layout()

plt.savefig('sin.png')


plt.show()