'''
小汽车质量等级预测
'''
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.preprocessing as sp #数据预处理
import sklearn.ensemble as se #集成学习
import sklearn.model_selection as ms #模型选择

data = pd.read_csv('../data_test/car.txt',
                   header=None)
# print(data.dtypes)

#标签编码，将字符串转为数值
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
model = se.RandomForestClassifier(max_depth=13,
                                  n_estimators=140,
                                  random_state=7,
                                  class_weight='balanced')
#验证曲线，寻找模型参数取值
# params = np.arange(6,16,1)
# train_score,test_score = ms.validation_curve(model,
#                                              train_x,train_y,
#                                              'max_depth',
#                                              params,
#                                              cv=5)
# avg_score = test_score.mean(axis=1)
# plt.plot(params,avg_score,'o-')
# plt.show()

#学习曲线，寻找最优的训练集测试集占比
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



#训练
model.fit(train_x,train_y)
#测试数据
test_data = [['high','med','5more','4','big','low','unacc'],
             ['high','high','4','4','med','med','acc'],
             ['low','low','2','4','small','high','good'],
             ['low','med','3','4','med','high','vgood']]
#将测试数据进行标签编码  '4'-》1
test_data = pd.DataFrame(test_data)
for i in test_data:
    encoder = encoders[i]
    res = encoder.transform(test_data[i])
    test_data[i] = res
test_x = test_data.iloc[:,:-1]
test_y = test_data.iloc[:,-1]
#预测
pred_test_y = model.predict(test_x)
print('真实类别:',encoders[6].inverse_transform(test_y.values))
print('预测类别:',encoders[6].inverse_transform(pred_test_y))

#置信概率：预测时属于每个类别的概率是多少
print(pred_test_y)
print(model.predict_proba(test_x))




