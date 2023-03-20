# 01_chinese_emotion.py
# 中文文本情感分析

############################ 预处理 #############################
import paddle
import paddle.dataset.imdb as imdb
import paddle.fluid as fluid
import numpy as np
import os
import random
from multiprocessing import cpu_count

mydict = {} # key:字   value:编码值
code = 1 # 编码初始值
data_file = "data/hotel_discuss2.csv" # 原始样本文件
dict_file = "data/hotel_dict.txt" # 字典文件
encoding_file = "data/hotel_encoding.txt" # 编码后的样本文件
puncts = " \n" # 标点符号列表(要丢弃的标点符号放入该列表)

# 读取每个样本，取出评论部分，对每个字进行编码
with open(data_file, "r", encoding="utf-8-sig") as f:
    for line in f.readlines():
        line = line.strip() # 去除空格

        for ch in line: # 取出每个字
            if ch in puncts: # 在符号列表中
                continue

            if ch in mydict: # 在字典中
                continue
            else: # 不在字典中，未参与编码
                mydict[ch] = code
                code += 1
    mydict["<unk>"] = code # 未知字符编码(用于从未在数据集中出现的字编码)

# 将字典存入文件
with open(dict_file, "w", encoding="utf-8-sig") as f:
    f.write(str(mydict))
    print("保存字典文件结束.")

# 从字典文件中读取字典
def load_dict():
    with open(dict_file, "r", encoding="utf-8-sig") as f:
        new_dict = eval(f.readlines()[0]) # 取出第一行当做表达式执行
    return new_dict # 返回字典对象

# 对评论数据进行编码
new_dict = load_dict() # 读取字典文件内容
with open(data_file, "r", encoding="utf-8-sig") as f: # 原始样本
    with open(encoding_file, "w", encoding="utf-8-sig") as fw: # 经过编码后的样本
        for line in f.readlines(): # 读取每行
            line = line.replace("\n", "") # 去除换行符
            label = line[0] # 第一个字符为标签
            remark = line[2:] # 从第三个字符到末尾为评论部分

            for ch in remark: # 取出评论部分每个字
                if ch in puncts:
                    continue
                else:
                    fw.write(str(new_dict[ch]))#将编码值写入文件
                    fw.write(",")#每个字的编码值之间用逗号分隔
            fw.write("\t" + str(label) + "\n") # 写入tab,标签,换行符
print("数据预处理完成.")


######################## 模型定义、训练 ##########################

# 获取字典长度
def get_dict_len(dict_path):
    with open(dict_path, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()
        new_dict = eval(lines[0])
    return len(new_dict.keys())

# 将reader读取到的数据(句子,标签)转换为整型(从文件中读取出来为字符串类型)
def data_mapper(sample):
    dt, lbl = sample
    val = [int(word) for word in dt.split(",") if word.isdigit()]
    return val, int(lbl)

def train_reader(train_list_path):
    def reader():
        with open(train_list_path, "r", encoding="utf-8-sig") as f:
            lines = f.readlines()
            np.random.shuffle(lines) # 打乱样本

            for line in lines: # 取出每行
                data, label = line.split("\t")
                yield data, label
    return paddle.reader.xmap_readers(data_mapper, reader, cpu_count(), 1024)

# 模型定义
def lstm_net(input, input_dim):
    input = fluid.layers.reshape(input,
                                 [-1, 1],  # 形状
                                 inplace=True) # 替换掉原张量
    # 词嵌入层
    emb = fluid.layers.embedding(input=input,
                                 size=[input_dim, 128], # 词表大小，词嵌入维度
                                 is_sparse=True) # 稀疏格式(梯度下降效率高些)
    # 全连接层
    fc1 = fluid.layers.fc(input=emb, size=128)

    # 第一分支：LSTM + POOL
    lstm1, _ = fluid.layers.dynamic_lstm(input=fc1, size=128)
    lstm2 = fluid.layers.sequence_pool(input=lstm1, pool_type="max")

    # 第二分支
    conv = fluid.layers.sequence_pool(input=fc1, pool_type="max")

    # 输出层
    out = fluid.layers.fc([conv, lstm2], size=2, act="softmax")

    return out

dict_len = get_dict_len(dict_file) # 取字典长度

# 定义张量
rmk = fluid.layers.data(name="rmk",
                        shape=[1], # 长度可变张量将shape设置为1
                        dtype="int64",
                        lod_level=1) # 层级表示的可变长张量
label = fluid.layers.data(name="label", shape=[1], dtype="int64")

model = lstm_net(rmk, dict_len)

# 定义损失函数、优化器
cost = fluid.layers.cross_entropy(input=model, label=label)
avg_cost = fluid.layers.mean(cost)
optimizer = fluid.optimizer.AdamOptimizer(learning_rate=0.0001)
optimizer.minimize(avg_cost) # 指定优化的目标函数

# accuracy
acc = fluid.layers.accuracy(input=model, label=label)

# 执行器
place = fluid.CUDAPlace(0) # GPU上执行
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program()) # 初始化

# reader
reader = train_reader(encoding_file)
batch_train_reader = paddle.batch(reader, batch_size=128)

# feeder
feeder = fluid.DataFeeder(place=place, feed_list=[rmk, label])

# 开始训练
for epoch in range(10):
    for batch_id, data in enumerate(batch_train_reader()):
        train_cost, train_acc = exe.run(fluid.default_main_program(),
                                        feed=feeder.feed(data),
                                        fetch_list=[avg_cost, acc])
        if batch_id % 20 == 0:
            print("epoch:%d, batch:%d, cost:%.4f, acc:%.4f" %
                  (epoch, batch_id, train_cost[0], train_acc[0]))
print("模型训练结束.")

# 保存模型
model_save_dir = "model/"
if not os.path.exists(model_save_dir): # 目录不存在
    os.makedirs(model_save_dir)

fluid.io.save_inference_model(model_save_dir, # 保存目录
                              [rmk.name],# 推理时需要喂入的张量的名称
                              [model],#推理结果从哪里获取
                              exe)#执行器
print("模型保存完成.")


############################ 测试 ##############################
import paddle
import paddle.fluid as fluid
import numpy as np
import os

data_file = "data/hotel_discuss2.csv" # 原始样本文件
dict_file = "data/hotel_dict.txt" # 字典文件
encoding_file = "data/hotel_encoding.txt" # 编码后的样本文件
model_save_dir = "model/"
puncts = " \n" # 标点符号列表(要丢弃的标点符号放入该列表)

# 从字典文件中读取字典
def load_dict():
    with open(dict_file, "r", encoding="utf-8-sig") as f:
        new_dict = eval(f.readlines()[0]) # 取出第一行当做表达式执行
    return new_dict # 返回字典对象

# 使用字典对传入的句子进行编码
def encode_by_dict(remark, dict_encode):
    remark = remark.strip()
    if len(remark) <= 0:
        return []

    ret = [] # 编码后的列表
    for ch in remark:
        if ch in puncts:
            continue

        if ch in dict_encode: # 在字典中
            ret.append(dict_encode[ch])
        else: # 不在字典中
            ret.append(dict_encode["<unk>"])
    return ret

lods = []
new_dict = load_dict() # 加载字典
lods.append(encode_by_dict("总体来说房间非常干净,卫浴设施也相当不错,交通也比较便利", new_dict))
lods.append(encode_by_dict("酒店交通方便，环境也不错，正好是我们办事地点的旁边，感觉性价比还可以", new_dict))
lods.append(encode_by_dict("设施还可以，服务人员态度也好，交通还算便利", new_dict))
lods.append(encode_by_dict("酒店服务态度极差，设施很差", new_dict))
lods.append(encode_by_dict("我住过的最不好的酒店,以后决不住了,设施陈旧，服务态度也不好，还贵", new_dict))
lods.append(encode_by_dict("说实在的我很失望，我想这家酒店以后无论如何我都不会再去了", new_dict))

place = fluid.CPUPlace()
infer_exe = fluid.Executor(place)
infer_exe.run(fluid.default_startup_program())

base_shape = [[len(c) for c in lods]] # 获取每个句子长度
tensor_words = fluid.create_lod_tensor(lods, base_shape, place)#列表转可变长张量

# 加载模型
infer_prog, feed_names, fetch_targets = \
    fluid.io.load_inference_model(model_save_dir, infer_exe)
params = {feed_names[0]:tensor_words} # 参数字典
result = infer_exe.run(infer_prog,
                       feed=params,
                       fetch_list=fetch_targets)
for r in result[0]:
    print("负面概率:%.5f, 正面概率:%.5f" % (r[0], r[1]))