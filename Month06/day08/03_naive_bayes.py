'''
朴素贝叶斯分类器
'''
import numpy as np
import pandas as pd
import sklearn.model_selection as ms #模型选择
import sklearn.naive_bayes as nb #朴素贝叶斯
import sklearn.metrics as sm #评估模块
import matplotlib.pyplot as plt

data = pd.read_csv('../data_test/multiple1.txt',
                   header=None,
                   names=['x1','x2','y'])

x = data.iloc[:,:-1]
y = data.iloc[:,-1]

train_x,\
test_x,\
train_y,\
test_y = ms.train_test_split(x,y,
                             test_size=0.1,
                             random_state=7,
                             stratify=y)

model = nb.GaussianNB()
model.fit(train_x,train_y)
pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y,
                               pred_test_y))
#暴力绘制分类边界线(从类别进行反推)
# 1.将x1的最小值,到x1的最大值,拆出来200个点  np.linspace()
x1s = np.linspace(data['x1'].min(),data['x1'].max(),200)
# 2.将x2的最小值,到x2的最大值,拆出来200个点
x2s = np.linspace(data['x2'].min(),data['x2'].max(),200)
# 3.组合x1和x2的所有组合(4W个点)    for嵌套 (二维)
points = []
for x1 in x1s:
    for x2 in x2s:
        points.append([x1,x2])
points = pd.DataFrame(points,columns=['x1','x2'])
# 4.将4w个点带入模型中,得到预测类别
points_label = model.predict(points)
# 5.将4w个点使用散点图进行绘制,根据类别控制颜色   cmap=gray
plt.scatter(points['x1'],points['x2'],c=points_label,cmap='gray')
# 6.将样本数据的散点图画出来
plt.scatter(data['x1'],data['x2'],c=data['y'],cmap='brg')
plt.show()