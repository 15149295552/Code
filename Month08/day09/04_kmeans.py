'''K-means'''

import pandas as pd
import sklearn.cluster as sc #聚类
import matplotlib.pyplot as plt

data = pd.read_csv('../data_test/multiple3.txt',
                   header=None,
                   names=['x1','x2'])
# print(data.head())

model = sc.KMeans(n_clusters=4)
model.fit(data)

labels = model.labels_
center = model.cluster_centers_
# print(center)

plt.scatter(data['x1'],data['x2'],c=labels,cmap='brg')
plt.colorbar()
#画出几何中心
plt.scatter(center[:,0],center[:,1],s=300,
            color='black',marker='+')
plt.show()


pred_y = model.predict([[1.32,2.31]])
print(pred_y)












