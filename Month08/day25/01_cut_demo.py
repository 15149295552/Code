# 01_cut_demo.py
# 利用jieba库实现分词
import jieba

text = "吉林市长春药店"

# 精确模式
seg_list = jieba.cut(text, cut_all=False) # cut_all表示否是为全模式
for word in seg_list:
    print(word, end="/")
print("")

# 全模式
seg_list = jieba.cut(text, cut_all=True)
for word in seg_list:
    print(word, end="/")
print("")

# 搜索引擎模式
seg_list = jieba.cut_for_search(text)
for word in seg_list:
    print(word, end="/")
print("")


