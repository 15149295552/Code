# -*- coding: utf-8 -*-
# 01_keywords_extract_demo.py
# 利用TF-IDF、TextRank算法提取文本关键字
import math
import jieba
import jieba.posseg as psg
from gensim import corpora, models
from jieba import analyse
import functools
import numpy as np


# 加载停用词表
def get_stopword_list():
    stop_word_path = "stopword.txt"  # 停用词文件
    with open(stop_word_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    stopword_list = [w.replace("\n", "") for w in lines]

    return stopword_list


# 去除停用词
def word_filter(seg_list):
    filter_list = []  # 过滤后词列表
    for word in seg_list:  # 取出每个词
        if not word in stopword_list and len(word) > 1:  # 没有在停用词表中
            filter_list.append(word)

    return filter_list


# 加载数据集
def load_data(corpus_path):
    doc_list = []  # 文档列表
    with open(corpus_path, "r", encoding="utf-8") as f:  # 打开文件
        for line in f.readlines():
            line = line.strip()  # 去除空格
            seg_list = jieba.cut(line)  # 分词
            filter_list = word_filter(seg_list)  # 去除停用词
            doc_list.append(filter_list)  # 将分词并过滤停用词的结果存入文档列表
    return doc_list


# 计算IDF
def train_idf(doc_list):
    idf_dict = {}  # key:词   value:idf值
    tt_count = len(doc_list)  # 总文档数量

    for doc in doc_list:  # 遍历每个文档
        doc_set = set(doc)  # 将文档中的每个词加推入字典去重
        for word in doc:  # 遍历每个词
            if word not in idf_dict.keys():  # 不在字典中
                idf_dict[word] = 1
            else:  # 在字典中
                num = idf_dict[word]
                num += 1  # 文档数量加1
                idf_dict[word] = num
    # 计算每个文档的IDF
    for word, doc_cnt in idf_dict.items():
        idf_dict[word] = math.log(tt_count / (doc_cnt + 1.0))  # 计算log(D/(D_i+1))

    # 对于从来未出现过的词，计算一个默认的IDF值
    default_idf = math.log(tt_count / 1.0)
    return idf_dict, default_idf


# TF-IDF类
class TfIdf(object):
    def __init__(self, idf_dict, default_idf, word_list, kw_num):
        """
        构造方法
        :param idf_dict: 计算的IDF值的字典
        :param default_idf: 默认IDF值
        :param word_list: 文本分词列表
        :param kw_num: 关键词数量
        """
        self.word_list = word_list
        self.idf_dict = idf_dict
        self.default_idf = default_idf
        self.tf_dict = self.get_tf_dict()  # 计算词频
        self.kw_num = kw_num

    # 计算tf
    def get_tf_dict(self):
        tf_dict = {}  # key:词   value:词频
        for word in self.word_list:
            if word not in tf_dict.keys():  # 不在字典中
                tf_dict[word] = 1
            else:  # 在字典中
                num = tf_dict[word]
                num += 1
                tf_dict[word] = num
        total = len(self.word_list)  # 词语总数
        for word, word_cnt in tf_dict.items():
            tf_dict[word] = float(word_cnt) / total

        return tf_dict

    def get_tfidf(self):  # 计算tf-idf值
        tfidf_dict = {}  # key:词    value:tf-idf值
        for word in self.word_list:
            idf = self.idf_dict.get(word, self.default_idf)  # 取idf值，没有则赋默认值
            tf = self.tf_dict.get(word, 0)  # 取词频，没有则赋0
            tfidf_dict[word] = tf * idf  # 计算tf-idf并存入字典

        # 对每个词根据tf-idf值排序
        sort_list = sorted(tfidf_dict.items(),  # 待排序对象
                           key=lambda x: x[1],  # 根据键值对第二个值排序
                           reverse=True)  # 倒序排列
        top_list = sort_list[0:self.kw_num]  # 切出前K个词
        for k, v in top_list:
            print(k + ",", end=" ")
        print("")

def tfidf_extract(word_list, kw_num=20):
    doc_list = load_data("corpus.txt") # 读取语料库
    idf_dict, default_idf = train_idf(doc_list) # 计算idf
    tfidf_model = TfIdf(idf_dict, default_idf, word_list, kw_num) # 实例化对象
    tfidf_model.get_tfidf() # 计算tf-idf值并打印前K个最高的词

def textrand_extract(text, kw_num=20):
    kw = analyse.textrank(text, kw_num) # TextRank提取关键词
    for keyword in kw:
        print(keyword + ",", end=" ")
    print("")

if __name__ == "__main__":
    global stopword_list

    text = """在中国共产党百年华诞的重要时刻，在“两个一百年”奋斗目标历史交汇关键节点，
    党的十九届六中全会的召开具有重大历史意义。全会审议通过的《决议》全面系统总结了党的百年奋斗
    重大成就和历史经验，特别是着重阐释了党的十八大以来党和国家事业取得的历史性成就、发生的历史性变革，
    充分彰显了中国共产党的历史自觉与历史自信。"""

    stopword_list = get_stopword_list() # 读取停用词
    seg_list = jieba.cut(text) # 对测试文档进行分词
    filter_list = word_filter(seg_list) # 过滤停用词

    # TF-IDF算法提取
    print("TF-IDF算法提取结果:")
    tfidf_extract(filter_list)

    print("TextRank算法提取结果:")
    textrand_extract(text)