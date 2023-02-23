'''
波士顿房屋价格数据预测
'''
import sklearn.datasets as sd  # 数据集合
import sklearn.model_selection as ms  # 模型选择
import sklearn.metrics as sm #评估模块
import sklearn.linear_model as lm #线性模型
import sklearn.preprocessing as sp #数据预处理
import sklearn.pipeline as pl #数据管线

data = sd.load_boston()
# print(data.keys())
# print(data.filename)
# print(data.DESCR)
# print(data.feature_names)
# print(data.data.shape)
# print(data.target.shape)

x = data.data
y = data.target
# 划分训练集和测试集
train_x, \
test_x, \
train_y, \
test_y = ms.train_test_split(x, y,
                             test_size=0.2,#测试集占比
                             random_state=7)#随机种子
# 使用线性回归，岭回归，多项式回归 构建模型

def get_model(name,model):
    print('--------------',name,'-------------')
    model.fit(train_x,train_y)
    pred_test_y = model.predict(test_x)
    pred_train_y = model.predict(train_x)
    print('训练集:',sm.r2_score(train_y,pred_train_y))
    print('测试集:',sm.r2_score(test_y,pred_test_y))

model_dic = {'线性回归':lm.LinearRegression(),
             '岭回归':lm.Ridge(),
             '多项式回归':pl.make_pipeline(sp.PolynomialFeatures(2),
                                          lm.LinearRegression())}

for name,obj in model_dic.items():
    get_model(name,obj)










