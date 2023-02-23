'''英文分词'''
import nltk.tokenize as tk
import numpy as np
import sklearn.feature_extraction.text as ft #特征提取
import sklearn.preprocessing as sp

doc = "Are you curious about tokenization? Let's see how it works! We need to analyze a couple of sentences with punctuations to see it in action."
# 分句子
# sents = tk.sent_tokenize(doc)
# for i in range(len(sents)):
#     print('序号:',i+1,'句子:',sents[i])

#分单词
# words = tk.word_tokenize(doc)
# for i in range(len(words)):
#     print('序号:', i + 1, '单词:', words[i])

# tokenizer = tk.WordPunctTokenizer()
# words = tokenizer.tokenize(doc)
# for i in range(len(words)):
#     print('序号:', i + 1, '单词:', words[i])

#词袋模型
doc = 'This hotel is very bad. The toilet in this hotel smells bad. The environment of this hotel is very good.'
sents = tk.sent_tokenize(doc)
#构建词袋模型对象
cv = ft.CountVectorizer()
bow = cv.fit_transform(sents).toarray()
#词频
TF = sp.normalize(bow,norm='l1')
# print(TF)

#词频-逆文档频率  TF-IDF

cv = ft.CountVectorizer()
bow = cv.fit_transform(sents)

tt = ft.TfidfTransformer()
res = tt.fit_transform(bow).toarray()
res = np.round(res,3)
print(res)
print(cv.get_feature_names())

