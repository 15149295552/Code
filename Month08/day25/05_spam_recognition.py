# -*- coding: utf-8 -*-
# 05_spam_recognition.py
# 垃圾邮件识别
"""
数据：5000个正常邮件，5001个垃圾邮件
特征表示：TF-IDF作为文本特征表示
分类器：朴素贝叶斯、支持向量机
"""

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
    tokens = [t.strip() for t in tokens]
    return tokens


# 去除特殊符号
def remove_special_char(text):
    tokens = tokenize_text(text)  # 分词
    # 定义正则
    # escape:对需要转义的字符串进行转义处理
    pattern = re.compile("[{}]".format(re.escape(string.punctuation)))
    # 利用正则进行匹配，并过滤
    # filter:对序列进行过滤，返回过滤后的元素组成的新列表
    filtered_tokens = filter(None, [pattern.sub("", t) for t in tokens])
    filtered_text = " ".join(filtered_tokens)  # 每个元素间以空格分隔，返回新字符串
    return filtered_text


# 过滤停用词
def remove_stopwords(text):
    tokens = tokenize_text(text)  # 分词
    filter_tokens = [t for t in tokens if t not in stopword_list]
    filter_text = " ".join(filter_tokens)
    return filter_text


# 规范化处理
def normalize_corpus(corpus):
    result = []  # 处理结果

    for text in corpus:
        text = remove_special_char(text)  # 去除特殊符号
        text = remove_stopwords(text)  # 去除停用词
        result.append(text)

    return result


# 计算TF-IDF值
def tfidf_extrator(corpus):
    vec = TfidfVectorizer(min_df=1,  # 最低词频
                          norm="l2",  # 正则化
                          smooth_idf=True,  # 是否做平滑
                          use_idf=True)  # 是否采用IDF指标
    features = vec.fit_transform(corpus)  # 计算每个词的TF-IDF值
    return vec, features


# 读取数据集
def get_data():
    corpus = []  # 邮件内容
    labels = []  # 标签(0:垃圾邮件  1:正常邮件)

    # 读取正常邮件
    with open("ham_data.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            corpus.append(line)
            labels.append(1)

    # 读取垃圾邮件
    with open("spam_data.txt", "r", encoding="utf-8") as f:
        for line in f.readlines():
            corpus.append(line)
            labels.append(0)

    return corpus, labels


# 过滤空文档
def remove_empty_docs(corpus, labels):
    filtered_corpus = []
    filtered_labels = []

    for doc, label in zip(corpus, labels):
        if doc.strip():  # 去除空格后非空
            filtered_corpus.append(doc)
            filtered_labels.append(label)

    return filtered_corpus, filtered_labels


# 计算并打印分类指标
def print_metrics(labels, pred):
    # Accuracy
    accuracy = metrics.accuracy_score(labels, pred)
    # Precision
    precision = metrics.precision_score(labels, pred)
    # Recall
    recall = metrics.recall_score(labels, pred)
    # F1
    f1 = metrics.f1_score(labels, pred)

    print("正确率:%.4f, 查准率:%.4f, 召回率:%.4f, F1:%.4f" %
          (accuracy, precision, recall, f1))


if __name__ == "__main__":
    global stopword_list

    # 读取停用词表
    with open("stop_words.utf8", encoding="utf-8") as f:
        stopword_list = f.readlines()

    corpus, labels = get_data()  # 读取数据集
    corpus, labels = remove_empty_docs(corpus, labels)  # 去除空文档
    print("样本数量:", len(labels))

    # 划分训练集、测试集
    train_x, test_x, train_y, test_y = ms.train_test_split(corpus,
                                                           labels,
                                                           test_size=0.3,
                                                           random_state=36)
    # 规范化处理
    train_x = normalize_corpus(train_x)
    test_x = normalize_corpus(test_x)
    print("规范化处理结束.")

    # 计算TF-IDF作为文本特征表示
    tfidf_vec, train_features = tfidf_extrator(train_x)
    test_features = tfidf_vec.transform(test_x)

    # 定义分类器
    ## 朴素贝叶斯
    print("朴素贝叶斯模型:")
    nb_model = MultinomialNB() # 朴素贝叶斯
    nb_model.fit(train_features, train_y) # 训练
    nb_pred = nb_model.predict(test_features) # 使用测试集预测
    print_metrics(test_y, nb_pred) # 计算并打印分类指标

    ## 支持向量机
    print("\n支持向量机:")
    svm_model = SGDClassifier()
    svm_model.fit(train_features, train_y)# 训练
    svm_pred = svm_model.predict(test_features)
    print_metrics(test_y, svm_pred) # 计算并打印分类指标
