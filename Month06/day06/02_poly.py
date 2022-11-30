'''
多项式回归
'''
import pandas as pd
import sklearn.preprocessing as sp #数据预处理
import sklearn.linear_model as lm #线性模型
import sklearn.pipeline as pl #数据管线
import matplotlib.pyplot as plt

data = pd.read_csv('../data_test/Salary_Data.csv')

#整理输入与输出
x = data.iloc[:,:-1]
y = data.iloc[:,-1]

#构建模型
model = pl.make_pipeline(sp.PolynomialFeatures(3),#扩展特征
                         lm.LinearRegression())#线性回归
#训练模型
model.fit(x,y)
#预测
pred_y = model.predict(x)

plt.scatter(x,y,s=60)
plt.plot(x,pred_y,color='orangered')

plt.show()







