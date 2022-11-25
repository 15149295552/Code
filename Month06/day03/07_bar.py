'''
柱状图
'''

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,13)
apples = np.random.normal(60,10,12)

plt.bar(x-0.2,apples,
        width=0.4,
        color='green')

plt.xticks(x,fontsize=18)
plt.yticks(fontsize=18)

#橘子
oranges = np.random.normal(60,10,12)

plt.bar(x+0.2,oranges,
        width=0.4,
        color='orangered')

#将柱子的高度,标在图中
for i in range(len(x)):
    plt.text(x[i]-0.2,apples[i],
             int(apples[i]),
             fontsize=18,
             ha='center',
             va='bottom')

for i in range(len(x)):
    plt.text(x[i]+0.2,oranges[i],
             int(oranges[i]),
             fontsize=18,
             ha='center',
             va='bottom')



plt.show()






