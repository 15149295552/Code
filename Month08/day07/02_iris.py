'''
鸢尾花类别预测
'''
import sklearn.datasets as sd #数据集合
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as lm
import sklearn.model_selection as ms #模型选择
import sklearn.metrics as sm #评估模块

iris = sd.load_iris()
# print(iris.keys())
# print(iris.feature_names)
# print(iris.DESCR)
# print(iris.target_names)
# print(iris.data.shape)
# print(iris.target)

#将x特征与y类别整合成df
data = pd.DataFrame(iris.data,
                    columns=iris.feature_names)
data['target'] = iris.target

#萼片可视化
data.plot.scatter(x='sepal length (cm)',
                  y='sepal width (cm)',
                  c='target',
                  cmap='brg')
#花瓣可视化
data.plot.scatter(x='petal length (cm)',
                  y='petal width (cm)',
                  c='target',
                  cmap='brg')

# plt.show()

#从样本数据中取出2个类别(1,2)，做二分类
# sub_data = data.iloc[50:]
# sub_data = data.tail(100)
# sub_data = data[(data.target == 1) | (data.target == 2)]
# sub_data = data[data.target != 0]
# sub_data = data[~(data.target==0)]
#整理输入数据
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
#划分训练集测试集
train_x,\
test_x,\
train_y,\
test_y = ms.train_test_split(x,y,
                             test_size=0.2,
                             random_state=7,
                             stratify=y)#按照类别进行等比划分
#构建模型
model = lm.LogisticRegression(solver='liblinear')
#在构建模型之后，开始训练之前，搞5次交叉验证
# score = ms.cross_val_score(model,
#                            x,y,
#                            cv=5,
#                            scoring='f1_weighted')
# print(score.mean())


#训练
model.fit(train_x,train_y)
#预测
pred_test_y = model.predict(test_x)
#评估(准确率：对的个数/样本总数)
print('真实类别:',test_y.values)
print('预测类别:',pred_test_y)

print((test_y == pred_test_y).sum() / test_y.size)
print('准确率:',sm.accuracy_score(test_y,pred_test_y))
print('查准率:',sm.precision_score(test_y,pred_test_y,
                                average='macro'))#不考虑权重，计算平均值
print('召回率:',sm.recall_score(test_y,pred_test_y,
                             average='macro'))
print('f1_score:',sm.f1_score(test_y,pred_test_y,
                              average='macro'))
print('混淆矩阵:\n',sm.confusion_matrix(test_y,
                                    pred_test_y))
print('分类报告:\n',sm.classification_report(test_y,
                                         pred_test_y))
