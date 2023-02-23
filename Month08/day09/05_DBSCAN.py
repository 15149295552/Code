'''DBSCAN'''

import pandas as pd
import sklearn.cluster as sc #聚类
import matplotlib.pyplot as plt

data = pd.read_csv('../data_test/multiple3.txt',
                   header=None,
                   names=['x1','x2'])
# print(data.head())

model = sc.DBSCAN(eps=0.65,
                  min_samples=5)
model.fit(data)

labels = model.labels_
# print(labels)


plt.scatter(data['x1'],data['x2'],c=labels,cmap='brg')
plt.colorbar()
plt.show()












