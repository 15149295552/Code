'''
基于Sklearn提供的接口实现线性回归
'''
import pandas as pd
import sklearn.linear_model as lm #线性模型
import matplotlib.pyplot as plt
import sklearn.metrics as sm #模型评估模块
import pickle

#数据准备
data = pd.read_csv('../data_test/Salary_Data.csv')
# print(data.head())

#整理输入(二维)与输出数据(一维)
#所有行,不要最后一列
x = data.iloc[:,:-1]
#所有行,只要最后一列
y = data.iloc[:,-1]

#构建模型
model = lm.LinearRegression()
#训练模型
model.fit(x,y)
#预测
pred_y = model.predict(x)
#打印权重,偏置
print('w1:{},w0:{}'.format(model.coef_[0],#权重
                           model.intercept_))#偏置

#散点图,及回归线可视化
# plt.scatter(x,y,s=60)
# plt.plot(x,pred_y,color='orangered')
# plt.show()

#在全部数据中,取到一部分数据,作为测试集(假设测试集没参加过训练)
test_x = x.iloc[::4] #测试集的输入
test_y = y[::4] #测试集输出(真实数据)
pred_test_y = model.predict(test_x)#预测数据

print('平均绝对误差:',sm.mean_absolute_error(test_y,pred_test_y))
print('平均平方误差:',sm.mean_squared_error(test_y,pred_test_y))
print('中位数绝对偏差:',sm.median_absolute_error(test_y,pred_test_y))
print('r2得分:',sm.r2_score(test_y,pred_test_y))

#保存模型
with open('model.pickle','wb') as f:
    pickle.dump(model,f)
print('模型保存成功')

#加载模型
with open('./model.pickle','rb') as f:
    new_model = pickle.load(f)

print(new_model.predict([[1.1],[2.2],[3.3]]))

