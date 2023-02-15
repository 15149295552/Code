'''
条形图，柱状图
'''
import numpy as np
import matplotlib.pyplot as plt

#随机生成1-12月苹果的销量
x = np.arange(1,13)
apples = np.random.normal(60,10,12)

plt.bar(x-0.2,apples,width=0.4,color='green')
plt.xticks(x)

# for i in range(len(x)):
#     plt.text(x[i],apples[i],int(apples[i]),
#              ha='center',va='bottom')

#橘子
oranges = np.random.normal(60,10,12)
plt.bar(x+0.2,oranges,width=0.4,color='orangered')

for i in range(len(x)):
    plt.text(x[i]-0.2,apples[i],int(apples[i]),
             ha='center',va='bottom')

for i in range(len(x)):
    plt.text(x[i]+0.2,oranges[i],int(oranges[i]),
             ha='center',va='bottom')



plt.show()




