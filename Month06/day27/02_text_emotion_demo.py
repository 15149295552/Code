# 02_text_emotion_demo.py
# 文本情感分析(本质上是二分类问题，将文本分为正面、负面情绪)

############################### 预处理 #################################
import paddle
import paddle.fluid as fluid
import numpy as np
import os
import random
from multiprocessing import cpu_count

word_dict = {}  # 存放每个字的编码   key:字  value:编码值  {"好":1, "你":2}
data_file = "data/hotel_discuss2.csv"  # 原始数据集
dict_file = "data/hotel_dict.txt"  # 字典文件
encoding_file = "data/hotel_encoding.txt"  # 经过编码后的数据集(每个字用数字替代)
puncts = " \n"  # 要过滤的标点符号列表
code = 1  # 编码初始值

# 读取出数据集中每条数据中的每个字，对每个字产生一个编码值
with open(data_file, "r", encoding="utf-8-sig") as f:
    for line in f.readlines():  # 遍历每行
        line = line.strip()  # 去空格
        for ch in line:  # 遍历每个字
            if ch in puncts:  # 当前字符在符号列表中
                continue

            if ch in word_dict:  # 已经在字典中，已经参与过编码
                continue
            else:  # 没有在字典中，产生一个编码值，填到字典
                word_dict[ch] = code
                code += 1
    word_dict["<unk>"] = code  # 未知字符(在数据集中没有出现过)编码

# 将字典内容存入文件，训练、测试阶段都使用同一个字典编码，保证编码规则一致
with open(dict_file, "w", encoding="utf-8-sig") as f:
    f.write(str(word_dict))  # 字典内容转换为字符串，写入文件
    print("保存字典文件结束.")


# 加载字典内容
def load_dict():
    with open(dict_file, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()
        new_dict = eval(lines[0])  # 取出第一行，当做表达式执行
    return new_dict


# 对原始数据集进行编码
new_dict = load_dict()
with open(data_file, "r", encoding="utf-8-sig") as f:  # 打开原始数据集
    with open(encoding_file, "w", encoding="utf-8-sig") as fw:
        for line in f.readlines():  # 从原始数据集中循环读取
            label = line[0]  # 类别
            remark = line[2:-1]  # 评论部分

            for ch in remark:  # 遍历每个字，从字典中取出编码值
                if ch in puncts:
                    continue

                fw.write(str(new_dict[ch]))
                fw.write(",")
            fw.write("\t" + str(label) + "\n")  # tab分隔符、标签值、换行符
print("数据预处理完成.")


########################### 模型定义、训练 ##############################

# 获取字典长度
def get_dict_len(dict_path):
    with open(dict_path, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()
        new_dict = eval(lines[0])  # 取出字典文件第一行，转换为字典对象
    return len(new_dict.keys())


def data_mapper(sample):
    remark, label = sample  # 赋值
    val = [int(word) for word in remark.split(",") if word.isdigit()]
    return val, int(label)  # 返回整形列表、标签


def train_reader(train_list_path):  # 训练集reader
    def reader():
        with open(train_list_path, "r", encoding="utf-8-sig") as f:
            lines = f.readlines()
            np.random.shuffle(lines)  # 顺序打乱

            for ln in lines:  # 取出每行
                data, label = ln.split("\t")  # 按tab拆分
                yield data, label

    return paddle.reader.xmap_readers(data_mapper,  # reader读取的数据下一步处理
                                      reader,  # 读取数据文件函数
                                      cpu_count(),  # 线程数量
                                      1024)  # 缓冲区大小


def lstm_net(input, input_dim):  # 定义模型
    # 对输入张量进行变维，变成列N行1列
    input = fluid.layers.reshape(input,  # 输入
                                 [-1, 1],  # 形状
                                 inplace=True)  # 替换原张量
    # 词嵌入层
    emb = fluid.layers.embedding(input=input,  # 输入
                                 size=[input_dim, 128],  # 词表大小、嵌入长度
                                 is_sparse=True)  # 稀疏格式
    # 第一层fc
    fc1 = fluid.layers.fc(input=emb, size=128)

    # 并列两个分支
    ## 第一分支：LSTM+池化
    lstm1, _ = fluid.layers.dynamic_lstm(input=fc1, size=128)
    lstm2 = fluid.layers.sequence_pool(input=lstm1, pool_type="max")
    ## 第二分支：池化
    conv = fluid.layers.sequence_pool(input=fc1, pool_type="max")

    # 输出层
    out = fluid.layers.fc([conv, lstm2], size=2, act="softmax")
    return out


dict_len = get_dict_len(dict_file)  # 取词典长度

# 张量占位符  lod_level不为0则为序列数据(长度变化)
rmk = fluid.layers.data(name="rmk", shape=[1], dtype="int64", lod_level=1)
label = fluid.layers.data(name="label", shape=[1], dtype="int64")

model = lstm_net(rmk, dict_len)  # 模型

# 损失函数、优化器
cost = fluid.layers.cross_entropy(input=model, label=label)
avg_cost = fluid.layers.mean(cost)  # 求均值
optimizer = fluid.optimizer.Adam(learning_rate=0.0001)  # 优化器
optimizer.minimize(avg_cost)  # 指定优化的目标函数
# Accuracy
accuracy = fluid.layers.accuracy(input=model, label=label)

# 执行器
place = fluid.CUDAPlace(0)  # GPU
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())  # 初始化

# reader
reader = train_reader(encoding_file)
batch_train_reader = paddle.batch(reader, batch_size=128)

# feeder
feeder = fluid.DataFeeder(place=place, feed_list=[rmk, label])

for epoch in range(40):  # 外层循环控制轮次
    for batch_id, data in enumerate(batch_train_reader()):  # 内层循环控制批次
        c, a = exe.run(fluid.default_main_program(),  # 执行默认program
                       feed=feeder.feed(data),  # 喂入数据
                       fetch_list=[avg_cost, accuracy])  # 返回损失值、正确率
        if batch_id % 20 == 0:
            print("epoch:%d, batch:%d, cost:%.5f, accuracy:%.5f"
                  % (epoch, batch_id, c[0], a[0]))
print("模型训练结束.")

# 保存推理模型
model_save_dir = "model/"
if not os.path.exists(model_save_dir):
    os.makedirs(model_save_dir)

fluid.io.save_inference_model(model_save_dir,  # 模型保存路径
                              [rmk.name],  # 模型推理喂入的张量名称
                              [model],  # 推理结果从哪里获取
                              exe)  # 执行器
print("保存推理模型成功.")

############################### 测试 ##################################

import paddle
import paddle.fluid as fluid
import numpy as np
import os
import random
from multiprocessing import cpu_count

data_file = "data/hotel_discuss2.csv"  # 原始数据集
dict_file = "data/hotel_dict.txt"  # 字典文件
encoding_file = "data/hotel_encoding.txt"  # 经过编码后的数据集(每个字用数字替代)
model_save_dir = "model/"  # 模型保存路径
puncts = " \n"  # 要过滤的标点符号列表

def load_dict():  # 加载字典内容
    with open(dict_file, "r", encoding="utf-8-sig") as f:
        lines = f.readlines()
        new_dict = eval(lines[0])
    return new_dict


# 使用字典对评论句子进行编码
def encode_by_dict(remark, dict_encoded):
    remark = remark.strip()
    if len(remark) <= 0:
        return []

    ret = []  # 编码结果
    for ch in remark:  # 从评论语句中取出每个字
        if ch in puncts: # 如果在指定符号列表中，跳过
            continue

        if ch in dict_encoded:
            ret.append(dict_encoded[ch])  # 存在，取出编码值添加到列表
        else:  # 字不在字典中，取未知字符的编码值
            ret.append(dict_encoded["<unk>"])
    return ret

lods = [] # 待预测句子列表
new_dict = load_dict() # 加载字典

lods.append(encode_by_dict("总体来说房间非常干净,卫浴设施也相当不错,交通也比较便利", new_dict))
lods.append(encode_by_dict("酒店交通方便，环境也不错，正好是我们办事地点的旁边，感觉性价比还可以", new_dict))
lods.append(encode_by_dict("设施还可以，服务人员态度也好，交通还算便利", new_dict))
lods.append(encode_by_dict("酒店服务态度极差，设施很差", new_dict))
lods.append(encode_by_dict("我住过的最不好的酒店,以后决不住了", new_dict))
lods.append(encode_by_dict("说实在的我很失望，我想这家酒店以后无论如何我都不会再去了", new_dict))

base_shape = [[len(c) for c in lods]] # 取出每个句子长度

# 执行器
place = fluid.CPUPlace()
infer_exe = fluid.Executor(place)
infer_exe.run(fluid.default_startup_program())

# 创建LOD Tensor
tensor_words = fluid.create_lod_tensor(lods, base_shape, place)

# 加载模型
infer_program, feed_vars, fetch_targets = \
    fluid.io.load_inference_model(model_save_dir, infer_exe)
# 参数字典
params = {feed_vars[0] : tensor_words}
# 执行推理
results = infer_exe.run(infer_program, # 执行推理program
                        feed=params, # 喂入参数
                        fetch_list=fetch_targets) # 指定返回结果
for r in results[0]: # 解析预测结果
    print("负面概率:%.4f, 正面概率:%.4f" % (r[0], r[1]))




