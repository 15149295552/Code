'''凝聚层次'''

import pandas as pd
import sklearn.cluster as sc #聚类
import matplotlib.pyplot as plt
import sklearn.metrics as sm

data = pd.read_csv('../data_test/multiple3.txt',
                   header=None,
                   names=['x1','x2'])
# print(data.head())

model = sc.AgglomerativeClustering(n_clusters=4)

model.fit(data)

labels = model.labels_
# print(labels)


plt.scatter(data['x1'],data['x2'],c=labels,cmap='brg')
plt.colorbar()
plt.show()

print(sm.silhouette_score(data,
                          labels,
                          sample_size=len(data)))

休息15分钟，16:25回来！！！！








