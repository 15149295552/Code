# 03_pos_demo.py
# 利用jieba实现分词、词性标注
import jieba.posseg as psg


def pos(text):
    results = psg.cut(text)  # 分词、词性标注
    for w, t in results:
        print("%s/%s" % (w, t), end=" ")
    print("")


text = "梅兰芳大剧院周六晚上有演出"
pos(text)

text = "超哥哥说他是赵丽颖的梦中情人"
pos(text)