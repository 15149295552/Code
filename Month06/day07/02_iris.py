'''
鸢尾花类别预测
'''
import sklearn.datasets as sd  # 数据集合
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.model_selection as ms  # 模型选择
import sklearn.linear_model as lm  # 线性模型
import sklearn.metrics as sm  # 评估模块

iris = sd.load_iris()
# print(iris.keys())
# print(iris.feature_names)
# print(iris.DESCR) # 150个样本,4个特征  3个类别
# print(iris.target_names)
# print(iris.data.shape)#(150,4)
# print(iris.target.shape) #(150,)

data = pd.DataFrame(iris.data,
                    columns=iris.feature_names)
data['target'] = iris.target

# 萼片可视化
plt.figure('sepal')
plt.scatter(data['sepal length (cm)'],
            data['sepal width (cm)'],
            c=data['target'],
            s=50,
            cmap='brg')
plt.colorbar()

# 花瓣可视化
plt.figure('petal')
plt.scatter(data['petal length (cm)'],
            data['petal width (cm)'],
            c=data['target'],
            s=50,
            cmap='brg')
plt.colorbar()
# plt.show()


# 拿到1类别和2类别的数据,做二分类
# sub_data = data.iloc[50:]
# sub_data = data.tail(100)
# sub_data = data[(data['target'] == 1) | (data['target'] == 2)]
# sub_data = data[~(data['target'] == 0)]  #~取反
# print(sub_data)

# 整理输入和输出
x = data.iloc[:, :-1]
y = data.iloc[:, -1]

# 划分训练集和测试集
train_x, \
test_x, \
train_y, \
test_y = ms.train_test_split(x, y,
                             test_size=0.2,
                             random_state=7,
                             stratify=y)  # 按照类别进行等比划分
# 构建模型
model = lm.LogisticRegression(solver='liblinear')

# 在模型构建之后,开始训练之前,使用交叉验证
# score = ms.cross_val_score(model,
#                            x, y,
#                            cv=5,
#                            scoring="f1_weighted")
# print(score.mean())
#训练
model.fit(train_x,train_y)
#预测
pred_test_y = model.predict(test_x)
#评估
#精度:准确率(预测对的个数 / 总的样本个数)
print('真实类别:',test_y.values)
print('预测类别:',pred_test_y)
# print('精度:',(test_y == pred_test_y).sum() / test_y.size)
print('精度:',sm.accuracy_score(test_y,pred_test_y))
print('查准率:',sm.precision_score(test_y,
                                  pred_test_y,
                                  average='macro'))
print('召回率:',sm.recall_score(test_y,
                               pred_test_y,
                               average='macro'))
print('F1得分:',sm.f1_score(test_y,
                            pred_test_y,
                            average='macro'))

print('混淆矩阵:\n',sm.confusion_matrix(test_y,pred_test_y))

print('分类报告:\n',sm.classification_report(test_y,pred_test_y))







