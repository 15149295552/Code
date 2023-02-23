# 将Salary_Data2.csv中的数据，使用线性回归去拟合样本数据

import numpy as np
import pandas as pd
import sklearn.linear_model as lm
import matplotlib.pyplot as plt
import sklearn.metrics as sm #评估模块

data = pd.read_csv('../data_test/Salary_Data2.csv')
x = data.iloc[:,:-1]
y = data.iloc[:,-1]

model = lm.LinearRegression()
model_ridge = lm.Ridge(alpha=98)

model.fit(x,y)
model_ridge.fit(x,y)

pred_y = model.predict(x)
pred_y_ridge = model_ridge.predict(x)

plt.scatter(x,y)
plt.plot(x,pred_y,color='orangered')
plt.plot(x,pred_y_ridge,color='black')
plt.show()

#设定一系列的参数，使用每一个参数构建模型，对比r2得分
# test_x = x.iloc[:30:4]
# test_y = y[:30:4]

# params = np.arange(91,105,1)
# scores = []
# for param in params:
#     model = lm.Ridge(alpha=param)
#     model.fit(x,y)
#     pred_test_y = model.predict(test_x)
#     scores.append(sm.r2_score(test_y,pred_test_y))
#
# scores = pd.Series(scores,index=params)
#
# print('最优秀的模型参数:{},得分为:{}'.format(scores.idxmax(),
#                                          scores.max()))








