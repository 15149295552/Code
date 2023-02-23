'''
决策树
'''
import sklearn.datasets as sd #数据集合
import sklearn.model_selection as ms #模型选择
import sklearn.tree as st #决策树
import sklearn.metrics as sm #评估模块
import matplotlib.pyplot as plt
import sklearn.ensemble as se #集成学习
import pandas as pd

data = sd.load_boston()
x = data.data
y = data.target

train_x,\
test_x,\
train_y,\
test_y = ms.train_test_split(x,y,
                             test_size=0.1,
                             random_state=7)

model = st.DecisionTreeRegressor(max_depth=6,
                                 min_samples_split=5)
model.fit(train_x,train_y)
pred_train_y = model.predict(train_x)
pred_test_y = model.predict(test_x)
print('单颗决策树训练集:',sm.r2_score(train_y,pred_train_y))
print('单颗决策树测试集:',sm.r2_score(test_y,pred_test_y))
# #决策树可视化
# plt.figure(figsize=(15,9))
# st.plot_tree(model,feature_names=data.feature_names,
#              filled=True)
# plt.savefig('tree.png')
#
# plt.show()

#Adaboost
sub_model = st.DecisionTreeRegressor(max_depth=6)
model = se.AdaBoostRegressor(sub_model,
                             n_estimators=400,
                             random_state=7)
model.fit(train_x,train_y)
pred_train_y = model.predict(train_x)
pred_test_y = model.predict(test_x)
print('Adaboost训练集:',sm.r2_score(train_y,pred_train_y))
print('Adaboost测试集:',sm.r2_score(test_y,pred_test_y))

#特征重要性
fi = model.feature_importances_
# print(fi)

fi = pd.Series(fi,index=data.feature_names)
fi = fi.sort_values(ascending=False)
fi.plot.barh(rot=45) #pandas可视化

# plt.show()

#GBDT
model = se.GradientBoostingRegressor(max_depth=6,
                                     n_estimators=400,
                                     random_state=7)
model.fit(train_x,train_y)
pred_train_y = model.predict(train_x)
pred_test_y = model.predict(test_x)
print('GBDT训练集:',sm.r2_score(train_y,pred_train_y))
print('GBDT测试集:',sm.r2_score(test_y,pred_test_y))



