'''
svm支持向量机
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.model_selection as ms #模型选择
import sklearn.svm as svm #支持向量机
import sklearn.metrics as sm #评估模块

data = pd.read_csv('../data_test/multiple2.txt',
                   header=None,
                   names=['x1','x2','y'])
# print(data.head())


#整理输入输出
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
#划分训练集和测试集
train_x,\
test_x,\
train_y,\
test_y = ms.train_test_split(x,y,
                             test_size=0.1,
                             random_state=7,
                             stratify=y)
#构建模型
# model = svm.SVC(kernel='linear')
# model = svm.SVC(kernel='poly',degree=4)
# model = svm.SVC(kernel='rbf',gamma=0.1)
params = [{'kernel':['linear'],'C':[1,10,100]},
          {'kernel':['poly'],'degree':[2,3],'C':[1,10,100]},
          {'kernel':['rbf'],'gamma':[1,0.1,0.01],'C':[1,10,100]}]
model = ms.GridSearchCV(svm.SVC(),params,cv=5)

#训练模型
model.fit(train_x,train_y)
#预测
pred_test_y = model.predict(test_x)
#评估
print(sm.classification_report(test_y,
                               pred_test_y))

print(model.best_params_)
print(model.best_score_)
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

