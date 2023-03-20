# 01_wiki_corpus_embedding.py
# 利用维基百科语料库训练词向量

############################### 解压数据集 ######################################
import logging
import os
import os.path
from gensim.corpora import WikiCorpus

# 定义输入文件
input_file = "data/data104767/articles.xml.bz2"
# 输出文件
out_file = open("wiki.zh.text", "w", encoding="utf-8")

# 解压数据集
count = 0

wiki = WikiCorpus(input_file,  # 输入文件
                  lemmatize=False,  # 词性还原：否
                  dictionary={})  # 空字典
for text in wiki.get_texts():  # 逐个样本读取
    out_file.write(" ".join(text) + "\n")  # 将一个样本写入
    count += 1

    if count % 200 == 0:
        print("解压笔数:", count)

    if count >= 20000:  # 2万笔退出
        break

out_file.close()

################################## 分词 ########################################
import jieba
import jieba.analyse
import codecs


def process_wiki_text(src_file, dest_file):
    with codecs.open(src_file, "r", "utf-8") as f_in, \
            codecs.open(dest_file, "w", "utf-8") as f_out:
        num = 1

        for line in f_in.readlines():  # 读取
            line_seg = " ".join(jieba.cut(line))  # 分词
            f_out.writelines(line_seg)  # 写入目标文件
            num += 1

            if num % 200 == 0:
                print("分词完成笔数:", num)

process_wiki_text("wiki.zh.text", "wiki.zh.text.seg")  # 调用函数执行分词

################################ 训练词向量 #####################################
import logging
import sys
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence # 按行读取

logger = logging.getLogger(__name__)
# format: 指定输出的格式和内容，format可以输出很多有用信息，
# %(asctime)s: 打印日志的时间
# %(levelname)s: 打印日志级别名称
# %(message)s: 打印日志信息
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)

in_file = "wiki.zh.text.seg" # 输入文件(分词结果文件)
out_file1 = "wiki.zh.text.model" # 存模型
out_file2 = "wiki.zh.text.vector" # 存权重

# 定义Word2Vec对象
model = Word2Vec(LineSentence(in_file), # 输入(对象按行读取)
                 size=100, # 词嵌入维度(常用50~300之间)
                 window=3, # 窗口大小
                 min_count=5, # 最次词频(词语出现次数少于该值则忽略)
                 workers=multiprocessing.cpu_count()) # 线程数量(和CPU数量一致)
# 保存模型
model.save(out_file1) # 保存模型结构
model.wv.save_word2vec_format(out_file2, # 权重文件
                              binary=False) # 保存格式：文本格式

################################## 测试 #######################################
import gensim
from gensim.models import Word2Vec

# 加载模型
model = Word2Vec.load("wiki.zh.text.model")

# 打印语义相似度最高的词
result = model.most_similar(u"铁路")
for r in result:
    print(r)

print("----------------------------")

result = model.most_similar(u"中药")
for r in result:
    print(r)






