
import pandas as pd
import sklearn.linear_model as lm #线性模型
import matplotlib.pyplot as plt
import numpy as np
import sklearn.metrics as sm #评估模块

data = pd.read_csv('../data_test/Salary_Data2.csv')
# print(data.head())

#整理输入和输出
x = data.iloc[:,:-1]
y = data.iloc[:,-1]


#构建模型
model = lm.LinearRegression()
model_ridge = lm.Ridge(alpha=98)
#训练模型
model.fit(x,y)
model_ridge.fit(x,y)
#执行预测
pred_y = model.predict(x)
pred_y_ridge = model_ridge.predict(x)

plt.scatter(x,y,s=60)
plt.plot(x,pred_y,color='orangered')
plt.plot(x,pred_y_ridge,color='black')

# plt.show()

#调整岭回归的参数 alpha
#拿到一部分数据,作为测试集,(假设测试集没参加过训练)
test_x = x.iloc[:30:4]
test_y = y[:30:4]

params = np.arange(90,111,1)
#分别使用每个模型参数构建模型,评估r2得分
scores = {}
for param in params:
    model = lm.Ridge(alpha=param)
    model.fit(x,y)
    pred_test_y = model.predict(test_x)
    score = sm.r2_score(test_y,pred_test_y)
    scores[param] = score
    # print('参数:{},得分:{}'.format(param,score))

scores = pd.Series(scores)
print('最优秀的模型参数:{},得分:{}'.format(scores.idxmax(),
                                         scores.max()))




