# 03_pos.py
# jieba库分词、词性标注
import jieba.posseg as psg


def pos(text):  # 分词、词性标注
    result = psg.cut(text)
    for w, t in result:
        print("%s/%s" % (w, t), end=" ")
    print("")


text = "梅兰芳大剧院星期六晚上有演出"
pos(text)
