# 01_fruits_vgg.py
# 利用VGG实现图像分类

########################## 预处理 ############################
import os

name_dict = {"apple": 0, "banana": 1, "grape": 2,
             "orange": 3, "pear": 4}  # 名称-类别编号对应
data_root_path = "data/fruits/"  # 数据集所在目录
test_file_path = data_root_path + "test.txt"  # 测试集文件路径
train_file_path = data_root_path + "train.txt"  # 训练集文件路径
name_data_list = {}  # key:水果名称   value:图片路径列表


# 将图片存入name_data_list字典中
def save_to_dict(path, name):
    if name not in name_data_list:  # 不在字典中
        img_list = []
        img_list.append(path)
        name_data_list[name] = img_list
    else:  # 在字典中
        name_data_list[name].append(path)


# 遍历数据集，取出每个图片路径，添加到上面的字典中
dirs = os.listdir(data_root_path)  # 列出数据集中所有子目录
for d in dirs:
    sub_dir_path = data_root_path + d  # 子目录路径
    if os.path.isdir(sub_dir_path):  # 目录
        imgs = os.listdir(sub_dir_path)  # 列出所有图片
        for img in imgs:
            img_path = sub_dir_path + "/" + img  # 图片路径
            save_to_dict(img_path, d)  # 添加到字典
    else:  # 文件
        pass

# 划分训练集/测试集
with open(train_file_path, "w") as f:
    pass
with open(test_file_path, "w") as f:
    pass

i = 0
for name, img_list in name_data_list.items():  # 遍历字典
    num = len(img_list)  # 取每个类别样本数量
    print("%s: %d张" % (name, num))

    for img in img_list:
        line = "%s\t%d\n" % (img, name_dict[name])  # 拼一行
        if i % 10 == 0:  # 写入测试集
            with open(test_file_path, "a") as f:
                f.write(line)
        else:  # 写入训练集
            with open(train_file_path, "a") as f:
                f.write(line)
        i += 1
print("数据预处理完成.")

###################### 定义、训练模型 #########################
import paddle
import paddle.fluid as fluid
import numpy
import sys
import os
from multiprocessing import cpu_count
import time
import matplotlib.pyplot as plt


def train_mapper(sample):
    """
    根据传入的样本，读取图片数据
    :param sample: 元组, 格式：(图片路径, 类别)
    :return: 经过缩放、归一化处理后的图像数据
    """
    img_path, label = sample  # 取出路径，标签
    # 读取图像
    img = paddle.dataset.image.load_image(img_path)
    # 对图像进行简单变换（缩放、裁剪）
    img = paddle.dataset.image.simple_transform(
        im=img,  # 输入
        resize_size=128,  # 缩放成128*128
        crop_size=128,  # 裁剪图像大小
        is_color=True,  # 彩色图像
        is_train=True)  # 训练模式
    # 图像归一化(不归一化模型可能不收敛)
    img = img.astype("float32") / 255.0
    return img, label


# 从样本中读取一行
def train_r(train_list, buffered_size=1024):
    def reader():
        with open(train_list, "r") as f:  # 打开样本文件
            for line in f.readlines():
                line = line.strip().replace("\n", "")
                img_path, lbl = line.split("\t")  # 拆分
                yield img_path, int(lbl)

    return paddle.reader.xmap_readers(train_mapper,  # 二次处理函数
                                      reader,  # 原始reader
                                      cpu_count(),  # 线程数量
                                      buffered_size)  # 缓冲区


# 定义VGG
def vgg_bn_drop(image, type_size):
    def conv_block(input, num_filter, groups, dropouts):
        """
        内部函数，定义连续N个卷积层，1个池化层
        :param input:输入
        :param num_filter:卷积核数量
        :param groups:连续几个卷积层
        :param dropouts:每层对应的丢弃率(未使用)
        :return:计算结果
        """
        return fluid.nets.img_conv_group(
            input=input,  # 输入
            conv_filter_size=3,  # 卷积核大小
            conv_num_filter=[num_filter] * groups,  # 每层卷积核数量
            conv_act="relu",  # 激活函数
            conv_with_batchnorm=True,  # 使用Batch normalization
            pool_type="max",  # 池化类型
            pool_size=2,  # 池化区域大小
            pool_stride=2)  # 池化步长

    conv1 = conv_block(image, 64, 2, [0.0, 0.0])
    conv2 = conv_block(conv1, 128, 2, [0.0, 0.0])
    conv3 = conv_block(conv2, 256, 3, [0.0, 0.0, 0.0])
    conv4 = conv_block(conv3, 512, 3, [0.0, 0.0, 0.0])
    conv5 = conv_block(conv4, 512, 3, [0.0, 0.0, 0.0])

    drop = fluid.layers.dropout(x=conv5, dropout_prob=0.5)
    fc1 = fluid.layers.fc(input=drop, size=512, act=None)

    bn = fluid.layers.batch_norm(input=fc1, act="relu")
    drop2 = fluid.layers.dropout(x=bn, dropout_prob=0.0)

    fc2 = fluid.layers.fc(input=drop2, size=512, act=None)
    predict = fluid.layers.fc(input=fc2,
                              size=type_size,
                              act="softmax")
    return predict


# 定义reader
BATCH_SIZE = 32  # 批次大小

train_reader = train_r(train_file_path)  # 原始reader
rand_train_reader = paddle.reader.shuffle(train_reader, 1300)
batch_train_reader = paddle.batch(rand_train_reader, BATCH_SIZE)

# 张量占位符
image = fluid.layers.data(name="image",  # 名称
                          shape=[3, 128, 128],  # 形状
                          dtype="float32")  # 类型
label = fluid.layers.data(name="label",
                          shape=[1],
                          dtype="int64")

predict = vgg_bn_drop(image=image, type_size=5)  # 模型计算

# 损失函数
cost = fluid.layers.cross_entropy(input=predict,  # 预测值
                                  label=label)  # 标签值
avg_cost = fluid.layers.mean(cost)  # 求均值
# 优化器
optimizer = fluid.optimizer.Adam(learning_rate=0.000001)
optimizer.minimize(avg_cost)  # 指定优化的目标函数
# 正确率
accuracy = fluid.layers.accuracy(input=predict,  # 预测值
                                 label=label)  # 标签值

# 执行器
place = fluid.CUDAPlace(0)  # 0表示一个GPU
exe = fluid.Executor(place)
exe.run(fluid.default_startup_program())

feeder = fluid.DataFeeder(feed_list=[image, label],
                          place=place)
costs = []  # 记录损失值
accs = []  # 记录正确率
times = 0
batches = []  # 记录迭代批次

for epoch in range(20):  # 外层循环控制轮次
    for batch_id, data in enumerate(batch_train_reader()):
        times += 1

        c, a = exe.run(fluid.default_main_program(),  # main program
                       feed=feeder.feed(data),  # 喂入数据
                       fetch_list=[avg_cost, accuracy])  # 指定返回值
        if batch_id % 20 == 0:
            print("epoch:%d, batch:%d, cost:%.4f, acc:%.4f" %
                  (epoch, batch_id, c[0], a[0]))
            accs.append(a[0])  # 记录正确率
            costs.append(c[0])  # 记录损失值
            batches.append(times)  # 记录批次

# 训练完成后保存模型
model_save_dir = "model/"
if not os.path.exists(model_save_dir):
    os.makedirs(model_save_dir)
fluid.io.save_inference_model(model_save_dir,  # 保存目录
                              ["image"],  # 推理时传入的参数
                              [predict],  # 推理结果从哪里获取
                              exe)  # 执行器
print("模型保存完成.")

# 训练过程可视化
plt.figure("Trainning")
plt.title("Trainning")
plt.xlabel("iters", fontsize=14)
plt.ylabel("cost/accuracy", fontsize=14)
plt.plot(batches, costs, color="red", label="cost")
plt.plot(batches, accs, color="blue", label="accuracy")
plt.legend()
plt.grid()
plt.savefig("train.png")
plt.show()

########################### 测试 ############################
from PIL import Image


# 读取测试图像
def load_img(img_path):
    img = paddle.dataset.image.load_and_transform(img_path,  # 路径
                                                  128,  # 裁剪大小
                                                  128,  # 缩放大小
                                                  False)  # 非训练模式
    img = img.astype("float32") / 255.0  # 归一化
    return img


# 执行器
place = fluid.CPUPlace()
infer_exe = fluid.Executor(place)  # 专门用于推理的执行器
model_save_dir = "model/"
# 加载模型
infer_prog, feed_vars, fetch_targets = \
    fluid.io.load_inference_model(model_save_dir, infer_exe)

test_img = "apple_1.png"  # 测试图像
infer_imgs = []  # 存放测试图像数据
infer_imgs.append(load_img(test_img))  # 读取图像并添加到列表
infer_imgs = numpy.array(infer_imgs)  # 列表转数组(张量和数组类型兼容)

params = {feed_vars[0]: infer_imgs}  # 参数字典

# 执行推理
results = infer_exe.run(infer_prog,  # 执行推理program
                        feed=params,  # 参数字典
                        fetch_list=fetch_targets)  # 指定返回的结果
r = numpy.argmax(results[0][0])  # 取出第一张图像预测概率最高的索引
for k, v in name_dict.items():
    if r == v:  # 索引和类别编号相等
        print("预测结果:", k)  # 打印名称

img = Image.open(test_img)
plt.imshow(img)
plt.show()
