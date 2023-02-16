'''
基于sklearn提供的API实现线性回归
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.linear_model as lm #线性模型
import sklearn.metrics as sm #评估模块
import pickle

#加载数据
data = pd.read_csv('../data_test/Salary_Data.csv')
#整理输入(二维)和输出(一维)
x = data.iloc[:,:-1]
y = data.iloc[:,-1]

#构建模型
model = lm.LinearRegression()
#训练
model.fit(x,y)
print('权重:{}'.format(model.coef_[0]))
print('偏置:{}'.format(model.intercept_))
#预测
pred_y = model.predict(x)
#回归线可视化
plt.scatter(x,y)
plt.plot(x,pred_y,color='orangered')
# plt.show()

#从全部数据中，抽取一部分数据，用于测试(假设测试集没参加训练)
#测试集的数据格式要和训练集一致
test_x = x.iloc[::4]
test_y = y[::4] #真实值
pred_test_y = model.predict(test_x) #预测值

print('平均绝对误差:',sm.mean_absolute_error(test_y,pred_test_y))
print('平均平方误差:',sm.mean_squared_error(test_y,pred_test_y))
print('中位数绝对偏差:',sm.median_absolute_error(test_y,pred_test_y))
print('r2_得分:',sm.r2_score(test_y,pred_test_y))

#保存模型
with open('./lr.pickle','wb') as f:
    pickle.dump(model,f)
print('模型保存成功')

#加载模型
with open('./lr.pickle','rb') as f:
    new_model = pickle.load(f)

print(new_model.predict([[1.1],[2.2],[3.3]]))




