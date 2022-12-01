'''
波士顿房屋价格预测(回归)
'''
import pandas as pd
import matplotlib.pyplot as plt
import sklearn.datasets as sd  # 数据集合
import sklearn.model_selection as ms  # 模型选择
import sklearn.metrics as sm #评估模块
import sklearn.linear_model as lm #线性模型
import sklearn.pipeline as pl #数据管线
import sklearn.preprocessing as sp #数据预处理
import sklearn.tree as st #决策树模块
import sklearn.ensemble as se #集成学习

boston = sd.load_boston()
# print(boston.keys())
# print(boston.filename)
# print(boston.DESCR)#506个样本,13列特征  1列输出
# print(boston.feature_names)
# print(boston.data.shape) # x
# print(boston.target.shape) # y

# 整理输入和输出
x = boston.data
y = boston.target

# 划分训练集和测试集
train_x,\
test_x,\
train_y,\
test_y = ms.train_test_split(x, y,#待划分的数据
                           test_size=0.1,#测试集占比
                           random_state=7)#随机种子,固定随机方式
# print(data[0].shape)# 训练集输入
# print(data[1].shape)# 测试集输入
# print(data[2].shape)# 训练集输出
# print(data[3].shape)# 测试集输出


def get_model(name,model):
    print('--------------------',name,'--------------------')
    model.fit(train_x,train_y)
    pred_test_y = model.predict(test_x)
    pred_train_y = model.predict(train_x)
    print('训练集:',sm.r2_score(train_y,pred_train_y))
    print('测试集:',sm.r2_score(test_y,pred_test_y))

model_dic = {'线性回归':lm.LinearRegression(),
             '岭回归':lm.Ridge(),
             '多项式回归':pl.make_pipeline(sp.PolynomialFeatures(2),
                                          lm.LinearRegression()),
             '单颗决策树':st.DecisionTreeRegressor(max_depth=4)}

# for name,obj in model_dic.items():
#     get_model(name,obj)


#Adaboost
model = st.DecisionTreeRegressor(max_depth=6)
model = se.AdaBoostRegressor(model,
                             n_estimators=400,
                             random_state=7)
model.fit(train_x,train_y)
pred_train_y = model.predict(train_x)
pred_test_y = model.predict(test_x)
print('Adaboost训练集:',sm.r2_score(train_y,pred_train_y))
print('Adaboost测试集:',sm.r2_score(test_y,pred_test_y))

#特征重要性
fi = model.feature_importances_

fi = pd.Series(fi,
               index=boston.feature_names)
#将特征重要性以柱状图的方式进行绘制
fi = fi.sort_values(ascending=False)#根据值降序排序
plt.bar(fi.index,fi.values)

# plt.show()


#GBDT
model = se.GradientBoostingRegressor(max_depth=6,
                                     n_estimators=400,
                                     min_samples_split=5)
model.fit(train_x,train_y)
pred_train_y = model.predict(train_x)
pred_test_y = model.predict(test_x)
print('GBDT训练集:',sm.r2_score(train_y,pred_train_y))
print('GBDT测试集:',sm.r2_score(test_y,pred_test_y))

#随机森林
model = se.RandomForestRegressor(max_depth=6,
                                 n_estimators=400,
                                 min_samples_split=5)
model.fit(train_x,train_y)
pred_train_y = model.predict(train_x)
pred_test_y = model.predict(test_x)
print('随机森林训练集:',sm.r2_score(train_y,pred_train_y))
print('随机森林测试集:',sm.r2_score(test_y,pred_test_y))


