# -*- coding: utf-8 -*-
# 02_spam_recognition.py
# 垃圾邮件识别案例
# 数据集：5000个正常邮件、5001个垃圾邮件
# 特征表示：TF-IDF表示特征
# 分类器：朴素贝叶斯、SVM
import numpy as np
import re
import string
import sklearn.model_selection as ms
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import SGDClassifier
from sklearn import metrics

import jieba
from sklearn.feature_extraction.text import TfidfVectorizer

label_name_map = ["垃圾邮件", "正常邮件"]


# 分词
def tokenize_text(text):
    tokens = jieba.cut(text)  # 分词
    tokens = [t.strip() for t in tokens]  # 取出元素，去除空格返回列表
    return tokens


# 过滤符号
def remove_special_char(text):
    tokens = tokenize_text(text)  # 分词
    # 定义正则对象
    # escape函数：自动对需要转义的字符串进行转义处理
    pattern = re.compile("[{}]".format(re.escape(string.punctuation)))
    # sub函数：使用正则对字符串进行匹配
    # filter函数：用于序列过滤，过滤掉不符合条件的元素，返回符合条件元素构成的列表
    filtered_tokens = filter(None, [pattern.sub("", t) for t in tokens])
    filtered_text = " ".join(filtered_tokens)  # 每个元素间添加空格
    return filtered_text

# 去除停用词
def remove_stopwords(text):
    tokens = tokenize_text(text) # 分词
    filtered_tokens = [t for t in tokens if t not in stopword_list]#去除停用词
    filtered_text = " ".join(filtered_tokens)
    return filtered_text

# 规范化处理
def normalize_corpus(corpus):
    result = [] # 处理结果

    for text in corpus:
        text = remove_special_char(text) # 去除特殊符号
        text = remove_stopwords(text) # 去除停用词
        result.append(text)

    return result

# 计算TF-IDF
def tfidf_extractor(corpus):
    vec = TfidfVectorizer(min_df=1, # 最低词频
                          norm="l2", # 正则化方法
                          smooth_idf=True, # 计算idf时是否做平滑处理
                          use_idf=True) # 是否使用idf指标
    features = vec.fit_transform(corpus)
    return vec, features # 返回对象、TF-IDF特征值


def get_data(): # 读取数据集
    corpus = [] # 邮件内容
    labels = [] # 邮件类别(0:垃圾邮件  1:正常邮件)

    # 正常邮件
    with open("ham_data.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            corpus.append(line) # 邮件内容
            labels.append(1) # 类别：正常邮件

    # 垃圾邮件
    with open("spam_data.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            corpus.append(line)
            labels.append(0) # 类别：垃圾邮件

    return corpus, labels

# 过滤空文档
def remove_empty_docs(corpus, labels):
    filtered_corpus = [] # 过滤后的邮件内容
    filtered_labels = [] # 过滤后的标签值

    for doc, label in zip(corpus, labels): # zip:从后面的可迭代对象中各取一个元素
        if doc.strip(): # 去除空格后，内容不为空串
            filtered_corpus.append(doc)
            filtered_labels.append(label)

    return filtered_corpus, filtered_labels

# 计算并打印分类指标
def print_metrics(labels, pred):
    # Accuracy
    accuracy = metrics.accuracy_score(labels, pred)
    # Precision
    precision = metrics.precision_score(labels, pred, average="weighted")
    # Recall
    recall = metrics.recall_score(labels, pred, average="weighted")
    # F1
    f1 = metrics.f1_score(labels, pred, average="weighted")

    print("正确率:%.2f, 查准率:%.2f, 召回率:%.2f, F1:%.2f" %
          (accuracy, precision, recall, f1))


if __name__ == "__main__":
    global stopword_list

    # 读取停用词表
    with open("stop_words.utf8", "r", encoding="utf-8") as f:
        stopword_list = f.readlines()

    # 读取数据集
    corpus, labels = get_data()
    corpus, labels = remove_empty_docs(corpus, labels) # 移除空文档
    print("样本数量:", len(labels))

    # 划分训练集、测试集
    train_x, test_x, train_y, test_y = ms.train_test_split(corpus, # 输入
                                                           labels, # 标签
                                                           test_size=0.3,#测试集比例
                                                           random_state=36)#随机种子
    # 规范化(取出符号、停用词)
    train_x = normalize_corpus(train_x)
    test_x = normalize_corpus(test_x)
    print("规范化处理结束.")

    # 计算TF-IDF
    vec, train_features = tfidf_extractor(train_x)#返回对象和TF-IDF
    test_features = vec.transform(test_x) # 使用同一个对象计算测试集TF-IDF
    print("计算训练集、测试集TF-IDF值结束.")

    # 使用朴素贝叶斯分类器
    print("朴素贝叶斯分类器:")
    nb_model = MultinomialNB() # 多项式朴素贝叶斯分类器
    nb_model.fit(train_features, train_y) # 训练(传入的x是TF-IDF特征向量，不是原邮件)
    nb_pred = nb_model.predict(test_features) # 使用测试集预测
    print_metrics(test_y, nb_pred) # 计算并打印分类指标
    print("")

    # 支持向量机
    print("支持向量机:")
    svm_model = SGDClassifier() # 线性分类器(包装了线性回归、SVC，默认为SVC)
    svm_model.fit(train_features, train_y) # 训练
    svm_pred = svm_model.predict(test_features)# 使用测试集预测
    print_metrics(test_y, svm_pred)# 计算并打印分类指标
    print("")