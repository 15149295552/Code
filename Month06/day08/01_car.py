'''
小汽车等级预测
作业:优先将训练集和测试集进行标签编码
    如果有能力,有时间,可以进行建模
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.preprocessing as sp #数据预处理
import sklearn.ensemble as se #集成学习
import sklearn.model_selection as ms #模型选择

data = pd.read_csv('../data_test/car.txt',
                   header=None)
# print(data.head())

#数据预处理:将字符串类型的数据,转为数值类型
#因为每列的离散值不同,为每列构建自己的标签编码器
train_data = pd.DataFrame()
encoders = {}
for i in data:
    encoder = sp.LabelEncoder()
    res = encoder.fit_transform(data[i])
    train_data[i] = res
    encoders[i] = encoder
#整理输入和输出
train_x = train_data.iloc[:,:-1]
train_y = train_data.iloc[:,-1]
#构建模型(随机森林)
#网格搜索,寻找最优的模型参数组合
params = {'max_depth':np.arange(10,16),#12
          'n_estimators':np.arange(50,301,50), #6
          'criterion':['gini','entropy']} #2

sub_model = se.RandomForestClassifier(class_weight='balanced',
                                      random_state=7)
model = ms.GridSearchCV(sub_model,params,cv=3)


#验证曲线,寻找最优的模型参数
# params = np.arange(11,21)
# train_score,\
# test_score = ms.validation_curve(model,#要测试的模型
#                                  train_x,train_y,#全部样本数据
#                                  'max_depth',#模型参数
#                                  params,#参数取值
#                                  cv=5)#交叉验证次数
# avg_score = test_score.mean(axis=1)
# plt.plot(params,avg_score,'o-') #o-连点成线
# plt.show()

#学习曲线:选取最优的训练集的大小
# params = np.arange(0.1,1.1,0.1)
# train_size,\
# train_score,\
# test_score = ms.learning_curve(model,
#                                train_x,train_y,
#                                train_sizes=params,
#                                cv=5)
# avg_score = test_score.mean(axis=1)
# plt.plot(params,avg_score,'o-')
# plt.show()

#训练集的数据,根本不够
# print(data[6].value_counts())

#训练
model.fit(train_x,train_y)

print('best_params:',model.best_params_)

test_data = [['high','med','5more','4','big','low','unacc'],
             ['high','high','4','4','med','med','acc'],
             ['low','low','2','4','small','high','good'],
             ['low','med','3','4','med','high','vgood']]


#预测
#预测数据的格式,要和训练数据一致(训练集做了标签编码,测试集也得做标签编码)
# 训练集和测试集的转换规则要一致
test_data = pd.DataFrame(test_data)
for i in test_data:
    #拿到训练集的编码器,过来转换测试机的数据
    encoder = encoders[i]
    res = encoder.transform(test_data[i])
    test_data[i] = res
#整理测试集的输入和输出
test_x = test_data.iloc[:,:-1]
test_y = test_data.iloc[:,-1]

pred_test_y = model.predict(test_x)
#评估
print('真实类别:',encoders[6].inverse_transform(test_y.values))
print('预测类别:',encoders[6].inverse_transform(pred_test_y))

#置信概率:预测时属于每个类别的概率
proba = model.predict_proba(test_x)
print(pred_test_y)
print(proba)


print(model)


