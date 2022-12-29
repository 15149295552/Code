# jieba库实现分词
import jieba

text = "吉林市长春药店"

seg_list = jieba.cut(text, cut_all=False)  # 精确模式
for word in seg_list:  # seg_list是生成器
    print(word, end="/")
print("")

seg_list = jieba.cut(text, cut_all=True) # 全模式
for word in seg_list:
    print(word, end="/")
print("")

seg_list = jieba.cut_for_search(text)
for word in seg_list:
    print(word, end="/")
print("")
