'''支持向量机'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.model_selection as ms #模型选择
import sklearn.svm as svm #支持向量机
import sklearn.metrics as sm #评估模块

data = pd.read_csv('../data_test/multiple2.txt',
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
# model = svm.SVC(kernel='linear')
# model = svm.SVC(kernel='poly',degree=3)
# model = svm.SVC(kernel='rbf',C=1.0,gamma=0.1)
params = [{'kernel':['linear'],'C':[1,10,100]},
          {'kernel':['poly'],'degree':[2,3],'C':[1,10,100]},
          {'kernel':['rbf'],'gamma':[1,0.1,0.01],'C':[1,10,100]}]
model = ms.GridSearchCV(svm.SVC(),params,cv=5)

model.fit(train_x,train_y)

print('最优的模型参数:',model.best_params_)
print('最优的得分:',model.best_score_)

pred_test_y = model.predict(test_x)
print(sm.classification_report(test_y,pred_test_y))

# print(model.coef_)
# print(model.intercept_)

# 1.将x1的最小值到x1的最大值拆分成200个点 np.linspace
x1s = np.linspace(data['x1'].min(),data['x1'].max(),200)
# 2.将x2的最小值到x2的最大值拆分成200个点
x2s = np.linspace(data['x2'].min(),data['x2'].max(),200)
# 3.组合x1和x2的所有情况 4W个点  forfor
points = []
for x1 in x1s:
    for x2 in x2s:
        points.append([x1,x2])
points = np.array(points)
# 4.将4W个点带入模型中，得到预测的类别  二维数据
points_label = model.predict(points)
# 5.将4W个点使用散点图绘制，颜色随着预测类别的变化而变化 cmap=gray
plt.scatter(points[:,0],points[:,1],c=points_label,
            cmap='gray')
# 6.再将样本的散点图进行绘制
plt.scatter(data['x1'],data['x2'],c=data['y'],cmap='brg')
plt.show()


