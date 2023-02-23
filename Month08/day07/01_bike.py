'''
共享单车投放量预测
'''
import pandas as pd
import sklearn.model_selection as ms #模型选择
import sklearn.ensemble as se #集成学习
import sklearn.metrics as sm #评估模块

data = pd.read_csv('../data_test/bike_day.csv')
# print(data.head())

data = data.drop(['instant', 'dteday', 'weekday',
                  'casual','registered'], axis=1)

#整理输入和输出
x = data.iloc[:,:-1]
y = data.iloc[:,-1]
#划分训练集和测试集
train_x,\
test_x,\
train_y,\
test_y = ms.train_test_split(x,y,
                             test_size=0.1,
                             random_state=7)
#构建模型
model = se.RandomForestRegressor(max_depth=10,
                                 n_estimators=1000,
                                 min_samples_split=5)
model.fit(train_x,train_y)
pred_test_y = model.predict(test_x)

print(sm.r2_score(test_y,pred_test_y))
print(sm.mean_absolute_error(test_y,pred_test_y))


