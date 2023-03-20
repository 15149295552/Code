# 02_tf_demo.py
# 统计高频词汇
import jieba


# 读取文件内容
def get_content(path):
    with open(path, "r", encoding="gbk") as f:
        content = ""  # 文件内容
        for line in f.readlines():
            line = line.strip()
            content += line  # 追加到content
    return content


# 读取停用词表
def get_stop_words(path):
    with open(path, encoding="utf-8") as f:
        return [ln.strip() for ln in f.readlines()]


def get_tf(words, topk=10):
    """
    统计词频
    :param words: 分词后的列表
    :param topk: 返回词的数量
    :return: 前K个词频最高的词
    """
    tf_dict = {}  # key:词    value:次数

    for w in words:
        if w not in tf_dict.keys():  # 不在字典中
            tf_dict[w] = 1
        else:  # 在字典中
            num = tf_dict[w]
            num += 1
            tf_dict[w] = num

    # 根据词语出现的次数倒序排列
    sorted_list = sorted(tf_dict.items(),  # 待排序对象
                         key=lambda x: x[1],  # 根据次数排序
                         reverse=True)  # 倒序排列
    return sorted_list[:topk]  # 返回前K个键值对


if __name__ == "__main__":
    corpus = get_content("11.txt") # 读取文件
    tmp_list = list(jieba.cut(corpus)) # 分词
    #print(tmp_list)
    stop_words = get_stop_words("stop_words.utf8")#读取停用词表

    # 过滤停用词
    split_words = [] # 过滤后的列表
    for w in tmp_list: # 遍历分词结果
        if w in stop_words: # 在停用词表中
            continue
        else: # 不在停用词表中
            split_words.append(w) #添加到列表

    print("\n分词结果:\n" + "/".join(split_words))

    topk_list = get_tf(split_words) # 统计词频，返回前10个高频词汇
    print("\nTop10词汇:", str(topk_list))