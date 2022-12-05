'''
Kmeans聚类
'''

import pandas as pd
import matplotlib.pyplot as plt
import sklearn.cluster as sc  #聚类模块

data = pd.read_csv('../data_test/multiple3.txt',
                   header=None,
                   names=['x1','x2'])
# print(data.head())

model = sc.KMeans(n_clusters=4)
model.fit(data)
#聚类结果
labels = model.labels_
#聚类中心
center = model.cluster_centers_
# print(center)
#散点图
plt.scatter(x=data['x1'],y=data['x2'],
            c=labels,
            cmap='brg')
plt.colorbar()
#几何中心
plt.scatter(x=center[:,0],y=center[:,1],
            c='black',
            marker='+',
            s=500)
plt.show()






