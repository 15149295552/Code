# -*- coding: utf-8 -*-
import pandas as pd
from collections import Counter

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.cluster import KMeans
import re
import string
import jieba


# 分词
def tokenize_text(text):
    tokens = jieba.cut(text)  # 分词
    tokens = [token.strip() for token in tokens]  # 去空格
    return tokens


def remove_special_characters(text):
    tokens = tokenize_text(text)
    pattern = re.compile('[{}]'.format(re.escape(string.punctuation)))
    filtered_tokens = filter(None, [pattern.sub('', token) for token in tokens])
    filtered_text = ' '.join(filtered_tokens)
    return filtered_text


# 去除停用词
def remove_stopwords(text):
    tokens = tokenize_text(text)  # 分词、去空格
    filtered_tokens = [token for token in tokens if token not in stopword_list]  # 去除停用词
    filtered_text = ''.join(filtered_tokens)
    return filtered_text


# 规范化处理
def normalize_corpus(corpus):
    result = []  # 处理结果

    for text in corpus:  # 遍历每个词汇
        text = remove_special_characters(text)  # 去除标点符号
        text = remove_stopwords(text)  # 去除停用词
        result.append(text)

    return result


# k_means聚类处理
def k_means(feature_matrix, num_clusters=10):
    km = KMeans(n_clusters=num_clusters, max_iter=10000)
    km.fit(feature_matrix)
    clusters = km.labels_
    return km, clusters


def get_cluster_data(clustering_obj, book_data,
                     feature_names, num_clusters,
                     topn_features=10):
    cluster_details = {}

    # 获取cluster的center
    ordered_centroids = clustering_obj.cluster_centers_.argsort()[:, ::-1]

    # 获取每个cluster的关键特征
    # 获取每个cluster的书
    for cluster_num in range(num_clusters):
        cluster_details[cluster_num] = {}
        cluster_details[cluster_num]['cluster_num'] = cluster_num
        key_features = [feature_names[index]
                        for index
                        in ordered_centroids[cluster_num, :topn_features]]
        cluster_details[cluster_num]['key_features'] = key_features

        books = book_data[book_data['Cluster'] == cluster_num]['title'].values.tolist()
        cluster_details[cluster_num]['books'] = books

    return cluster_details


def print_cluster_data(cluster_data):
    # print cluster details
    for cluster_num, cluster_details in cluster_data.items():
        print('Cluster {} details:'.format(cluster_num))
        print('-' * 20)
        print('Key features:', cluster_details['key_features'])
        print('book in this cluster:')
        print(', '.join(cluster_details['books']))
        print('=' * 40)


if __name__ == "__main__":
    global stopword_list  # 停用词列表

    # 读取停用词
    with open("dict/stop_words.utf8", encoding="utf8") as f:
        stopword_list = f.readlines()

    book_data = pd.read_csv('data/data.csv')  # 读取文件

    print(book_data.head())

    # 取出书名和内容
    book_titles = book_data['title'].tolist()
    book_content = book_data['content'].tolist()

    print('书名:', book_titles[0])
    print('内容:', book_content[0][:10])

    # 规范化处理(去除停用词和特殊符号)
    norm_book_content = normalize_corpus(book_content)

    # 提取 tf-idf 特征
    vectorizer = TfidfVectorizer()
    feature_matrix = vectorizer.fit_transform(book_content).astype(float)

    # 查看特征数量
    print("特征数量:", feature_matrix.shape)

    # 打印特征名称
    feature_names = vectorizer.get_feature_names()
    print("特征名称:", feature_names[:10])

    # 执行聚类
    num_clusters = 10  # 聚类数量
    km_obj, clusters = k_means(feature_matrix=feature_matrix, num_clusters=num_clusters)
    book_data['Cluster'] = clusters

    # 获取每个cluster的数量
    c = Counter(clusters)
    print(c.items())

    cluster_data = get_cluster_data(clustering_obj=km_obj,
                                    book_data=book_data,
                                    feature_names=feature_names,
                                    num_clusters=num_clusters,
                                    topn_features=5)

    print_cluster_data(cluster_data)
