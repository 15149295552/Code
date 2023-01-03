# 01_word_embedding_demo.py
# 利用中文维基百科语料库训练词向量
# 需要安装gensim软件包：pip install gensim==3.8.1


########################## 解压数据集 ############################
import logging
import os
import os.path
from gensim.corpora import WikiCorpus

input_file = "data/data104767/articles.xml.bz2"  # 输入数据(语料库文件)
out_file = open("wiki.zh.text", "w", encoding="utf-8")  # 解压输出文件

count = 0  # 计数器
wiki = WikiCorpus(input_file,  # 输入文件
                  lemmatize=False,  # 不做词性还原
                  dictionary={})
for text in wiki.get_texts():  # 逐笔取数据
    out_file.write(" ".join(text) + "\n")  # 写入一行
    count += 1

    if count % 200 == 0:
        print("读取笔数:", count)
    if count >= 20000:  # 2万笔时退出
        break
out_file.close()

############################# 分词 ##############################
import jieba
import jieba.analyse
import codecs


def process_wiki_text(src_file, dst_file):
    with codecs.open(src_file, "r", "utf-8") as f_in, \
            codecs.open(dst_file, "w", "utf-8") as f_out:  # 同时打开两个文件
        num = 1
        for line in f_in.readlines():  # 逐笔读取
            line_seg = " ".join(jieba.cut(line))  # 分词，在每个词之间加空格
            f_out.writelines(line_seg)  # 分词结果写入输出文件
            num += 1

            if num % 200 == 0:
                print("处理完成:", num)


process_wiki_text("wiki.zh.text", "wiki.zh.text.seg")

########################## 训练词向量 ############################
import logging
import sys
import multiprocessing
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence  # 按行读取

logger = logging.getLogger(__name__)
# format: 指定输出的格式和内容，format可以输出很多有用信息，
# %(asctime)s: 打印日志的时间
# %(levelname)s: 打印日志级别名称
# %(message)s: 打印日志信息
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
logging.root.setLevel(level=logging.INFO)

in_file = "wiki.zh.text.seg"  # 输入文件(分词的输出文件)
out_file1 = "wiki.zh.text.model"  # 模型保存文件
out_file2 = "wiki.zh.text.vector"  # 权重保存文件(词向量文件)

# 定义模型
model = Word2Vec(LineSentence(in_file),  # 输入
                 size=100,  # 词向量长度(建议50~300维之间)
                 window=3,  # 窗口大小
                 # sg=1, # 设置为1则使用skig-gram, 否则使用CBOW
                 min_count=5,  # 语料库出现的最低词频，低于该值忽略
                 workers=multiprocessing.cpu_count())  # 线程数量(保持和CPU数量一致)
model.save(out_file1)  # 保存模型结构
# 保存权重
model.wv.save_word2vec_format(out_file2,  # 文件路径
                              binary=False)  # 保存成txt格式，不保存为二进制
print("保存模型结束.")

############################# 测试 ##############################
import gensim
from gensim.models import Word2Vec

# 加载模型
model = Word2Vec.load("wiki.zh.text.model")
count = 0

for word in model.wv.index2word:
    print(word, model[word])  # 打印
    count += 1
    if count >= 10:
        break

print("==================================")

result = model.most_similar(u"铁路")
for r in result:
    print(r)

print("==================================")

result = model.most_similar(u"中药")
for r in result:
    print(r)
