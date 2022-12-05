'''
DBSCAN
'''

import pandas as pd
import matplotlib.pyplot as plt
import sklearn.cluster as sc  #聚类模块

data = pd.read_csv('../data_test/multiple3.txt',
                   header=None,
                   names=['x1','x2'])
# print(data.head())

model = sc.DBSCAN(eps=0.65,
                  min_samples=5)
model.fit(data)
#聚类结果
labels = model.labels_
print(labels)
#散点图
plt.scatter(x=data['x1'],y=data['x2'],
            c=labels,
            cmap='brg')
plt.colorbar()

plt.show()






