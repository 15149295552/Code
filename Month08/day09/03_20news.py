'''
邮件主题分类
'''
import sklearn.datasets as sd #数据集合
import sklearn.feature_extraction.text as ft#特征提取
import sklearn.model_selection as ms #模型选择
import sklearn.linear_model as lm #线性模型
import sklearn.metrics as sm #评估模块
import sklearn.naive_bayes as nb #朴素贝叶斯

data = sd.load_files('../data_test/20news',
                     random_state=7,
                     encoding='latin1')
# print(data.keys())
# print(data.data[0])
# print(data.target[0])
# print(data.target_names)

#构建词袋模型
cv = ft.CountVectorizer()
bow = cv.fit_transform(data.data)
#词频逆文档频率
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow)
# print(tfidf.shape)

x = tfidf
y = data.target
train_x,\
test_x,\
train_y,\
test_y = ms.train_test_split(x,y,
                             test_size=0.1,
                             random_state=7,
                             stratify=y)

# model = lm.LogisticRegression()
model = nb.MultinomialNB()

#交叉验证，验证逻辑回归
# scores = ms.cross_val_score(model,x,y,cv=5,
#                             scoring='f1_weighted')
# print(scores.mean())

model.fit(train_x,train_y)
pred_test_y = model.predict(test_x)
# print(sm.classification_report(test_y,pred_test_y))

#整理一组测试数据，进行模型的测试
# 1.在上一场比赛中，观众被棒球误伤砸中，已就医
# 2.最近老王在研究非对称加密算法
# 3.这两个轮的车在高速公路上跑的还挺快
# 4.明年中国将探索火星

test_data = ['At the last game, a spectator was hit by a baseball and was hospitalized.',
             'Recently, Lao Wang is working on asymmetric encryption algorithms.',
             'The two wheels are pretty fast on the highway.',
             'China will explore Mars next year.']
bow = cv.transform(test_data)
test_data = tt.transform(bow)
pred_y = model.predict(test_data)
print(pred_y)
print(data.target_names)

