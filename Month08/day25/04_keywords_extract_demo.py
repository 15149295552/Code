# -*- coding: utf-8 -*-
# 04_keywords_extract_demo.py
# 利用TF-DF、TextRank算法提取文档关键字

import math
import jieba
import jieba.posseg as psg
from gensim import corpora, models
from jieba import analyse
import functools
import numpy as np


# 读取停用词表
def get_stopword_list():
    with open("stopword.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
    stopword_list = [sw.replace("\n", "") for sw in lines]
    return stopword_list


# 过滤停用词
def word_filter(seg_list):
    filter_list = []  # 过滤后的列表
    for w in seg_list:  # 遍历每个词
        if not w in stopword_list and len(w) > 1:
            filter_list.append(w)
    return filter_list


# 读取语料库
def load_data(corpus_path):
    doc_list = []  # 文档列表

    with open(corpus_path, "r", encoding="utf-8") as f:
        for line in f.readlines():
            content = line.strip()  # 去空格
            seg_list = jieba.cut(content)  # 分词
            filter_list = word_filter(seg_list)  # 过滤停用词
            doc_list.append(filter_list)  # 加入列表

    return doc_list  # 返回经过分词、过滤停用词后的文档列表


# 计算idf值
def train_idf(doc_list):
    idf_dict = {}  # key:词   value:idf
    tt_count = len(doc_list)  # 总文档数量

    for doc in doc_list:  # 遍历每个文档
        doc_set = set(doc)  # 将文档的词汇填入列表去重

        for word in doc_set:
            if word in idf_dict.keys():  # 在字典中
                num = idf_dict[word]  # 取出出现的文档数量
                num += 1
                idf_dict[word] = num
            else:  # 不在字典中
                idf_dict[word] = 1

    # 计算idf值
    for word, doc_cnt in idf_dict.items():
        idf_dict[word] = math.log(tt_count / (doc_cnt + 1.0))

    # 对于从未在文档中出现过的词，计算一个默认idf
    default_idf = math.log(tt_count / 1.0)

    return idf_dict, default_idf


# TF-IDF计算类
class TfIdf(object):
    def __init__(self, idf_dict, default_idf, word_list, kw_num):
        """
        构造方法
        :param idf_dict: idf字典
        :param default_idf: 未出现词的默认idf值
        :param word_list: 待提取文本
        :param kw_num: 关键词数量
        """
        self.idf_dict = idf_dict
        self.default_idf = default_idf
        self.word_list = word_list
        self.kw_num = kw_num
        self.tf_dict = self.get_tf_dict()  # 调用内部方法，计算词频

    def get_tf_dict(self):  # 计算词频
        tf_dict = {}  # key:词   value:词频

        # 先用一趟循环统计每个词出现次数
        for word in self.word_list:
            if word in tf_dict.keys():  # 在字典中
                num = tf_dict[word]
                num += 1
                tf_dict[word] = num
            else:  # 不在字典中，第一次出现
                tf_dict[word] = 1

        # 计算词频
        total = len(self.word_list)  # 词语总数
        for word, word_cnt in tf_dict.items():
            tf_dict[word] = float(word_cnt) / float(total)

        return tf_dict

    def get_tfidf(self):  # 计算TF-IDF
        tfidf_dict = {}  # key:词  value:TF-IDF值

        for word in self.word_list:
            idf = self.idf_dict.get(word, self.default_idf)  # 取IDF值
            tf = self.tf_dict.get(word, 0)  # 取词频
            tfidf_dict[word] = tf * idf  # 计算TF-IDF并存入字典

        # 根据TF-IDF值倒序排列
        sorted_list = sorted(tfidf_dict.items(),  # 待排序对象
                             key=lambda x: x[1],  # 根据键值对第二个元素排序
                             reverse=True)  # 倒序排列
        # 打印前N个词
        top_list = sorted_list[0:self.kw_num]  # 取出前N个词
        for k, v in top_list:
            print(k + ",", end="")
        print()

def tfidf_extract(word_list, kw_num=20):
    doc_list = load_data("corpus.txt") # 读取语料库
    idf_dict, default_idf = train_idf(doc_list) # 计算每个词的idf值
    tfidf_model = TfIdf(idf_dict, default_idf, word_list, kw_num)
    tfidf_model.get_tfidf() # 计算TF-IDF并打印

# TextRank算提取
def textrank_extract(text, kw_num=20):
    keywords = analyse.textrank(text, kw_num)
    for kw in keywords:
        print(kw + ",", end="")
    print()


if __name__ == "__main__":
    global stopword_list

    text = """在中国共产党百年华诞的重要时刻，在“两个一百年”奋斗目标历史交汇关键节点，
    党的十九届六中全会的召开具有重大历史意义。全会审议通过的《决议》全面系统总结了党的百年奋斗
    重大成就和历史经验，特别是着重阐释了党的十八大以来党和国家事业取得的历史性成就、发生的历史性变革，
    充分彰显了中国共产党的历史自觉与历史自信。"""

    stopword_list = get_stopword_list() # 读取停用词表
    seg_list = jieba.cut(text) # 分词
    filter_list = word_filter(seg_list) # 停用词过滤

    # TF-IDF提取关键字
    print("TF-IDF提取结果:")
    tfidf_extract(filter_list)

    # TextRank提取
    print("TextRank提取结果:")
    textrank_extract(text)