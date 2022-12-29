# 分词、统计高频词汇
import jieba


# 读取文件内容
def get_content(path):
    with open(path, "r", encoding="gbk") as f:
        content = ""  # 读取到的内容
        for line in f.readlines():
            line = line.strip()
            content += line
    return content


# 统计词频，返回词频最高的K个词
def get_tf(words, topk=10):
    tf_dict = {}  # key:词  value:出现次数

    for w in words:
        if w not in tf_dict.keys():  # 没有在字典中，第一次出现
            tf_dict[w] = 1  # 次数设置为1
        else:  # 已经在字典中
            num = tf_dict[w]
            num += 1
            tf_dict[w] = num

    # 按照词语出现次数倒序排列
    sort_list = sorted(tf_dict.items(),  # 待排序对象
                       key=lambda x: x[1],  # 根据键值对的第二个元素排序
                       reverse=True)  # 倒序排列
    return sort_list[0:topk]


# 读取停用词
def get_stop_words(path):
    with open(path, encoding="utf8") as f:
        return [line.strip() for line in f.readlines()]


if __name__ == "__main__":
    # 读取文件内容
    corpus = get_content("11.txt")
    # 分词
    tmp_list = list(jieba.cut(corpus))
    # 读取停用词表
    stop_words = get_stop_words("stop_words.utf8")

    split_words = [] # 过滤掉停用词后的词列表
    for w in tmp_list:
        if w not in stop_words: # 该词不在停用词表中
            split_words.append(w)

    print("\n分词结果:\n" + "/".join(split_words))

    # 统计词频，返回前K个高频词汇
    tf_list = get_tf(split_words)
    print("\nTop10词汇:\n", str(tf_list))
