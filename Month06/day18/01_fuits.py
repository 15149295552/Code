# 01_fruits.py
# 利用CNN实现图像分类

##################### 预处理 #######################
import os

name_dict = {"apple": 0, "banana": 1, "grape": 2,
             "orange": 3, "pear": 4}
data_root_path = "data/fruits/"  # 数据集目录
test_file_path = data_root_path + "test.txt"  # 测试集文件
train_file_path = data_root_path + "train.txt"  # 训练集文件
name_data_list = {}  # key:水果名  value:图片路径列表


def save_to_dict(path, name):  # 将图片路径存入name_data_list
    if name not in name_data_list:  # 该类别不在字典中
        img_list = []
        img_list.append(path)  # 将路径存入列表
        name_data_list[name] = img_list  # 将列表存入字典
    else:  # 该类别已经在字典中
        name_data_list[name].append(path)


# 遍历数据集
dirs = os.listdir(data_root_path)
for d in dirs:
    sub_dir = data_root_path + d  # 子目录完整路径
    # print(sub_dir)

    if not os.path.isdir(sub_dir):  # 不是目录，跳过
        continue

    imgs = os.listdir(sub_dir)  # 列出子目录下所有图片
    for fn in imgs:  # 遍历每张图片文件
        img_path = sub_dir + "/" + fn  # 文件完整路径
        save_to_dict(img_path, d)  # 存入字典

# 将name_data_list中的内容写入训练集、测试集文件
with open(train_file_path, "w") as f:
    pass
with open(test_file_path, "w") as f:
    pass

for name, img_list in name_data_list.items():
    i = 0
    num = len(img_list)  # 每个类别图片数量
    print("%s: %d张" % (name, num))

    for img in img_list:  # 遍历每张图片路径
        line = "%s\t%d\n" % (img, name_dict[name])  # 一行
        if i % 10 == 0:  # 写入测试集
            with open(test_file_path, "a") as f:
                f.write(line)
        else:  # 写入训练集
            with open(train_file_path, "a") as f:
                f.write(line)
        i += 1
print("数据预处理结束.")

################## 模型定义、训练 ###################
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
    根据传入的文件路径、类别，读取图像数据并返回
    :param sample: 元组，格式为(路径，类别)
    :return: 图像张量、类别
    """
    img, label = sample  # 取出路径、类别
    # 读取图像
    img = paddle.dataset.image.load_image(img)
    # 对图像进行缩放
    img = paddle.dataset.image.simple_transform(
        im=img,  # 输入图像数据
        resize_size=128,  # 图像缩放到128*128
        crop_size=128,  # 裁剪图像大小
        is_color=True,  # 是否为彩色图像
        is_train=True)  # 训练模式(训练模式下会做随机裁剪)
    # 归一化(将像素值转换到0~1之间)
    # 归一化的作用：不做归一化可能不收敛；增加模型稳定性
    img = img.astype("float32") / 255.0
    return img, label  # 返回经过归一化的图像数据、标签


# 从训练集读取数据
def train_r(train_list, buffered_size=1024):
    def reader():
        with open(train_list, "r") as f:
            for line in f.readlines():  # 遍历每行
                line = line.replace("\n", "")  # 去换行符
                img_path, lbl = line.split("\t")
                yield img_path, int(lbl)  # 返回路径、类别

    return paddle.reader.xmap_readers(
        train_mapper,  # reader返回的数据进行下一步处理
        reader,  # 原始读取函数
        cpu_count(),  # 线程数量(和CPU数量一致)
        buffered_size)  # 缓冲区大小(预分配内存)


# 搭建CNN
def create_CNN(image, type_size):
    """
    定义CNN
    :param image: 经过归一化后的图像数据
    :param type_size: 分类数量
    :return: 模型计算结果
    """
    # 第一组 卷积池化+dropout
    conv_pool_1 = fluid.nets.simple_img_conv_pool(
        input=image,  # 输入：图像
        filter_size=3,  # 卷积核大小
        num_filters=32,  # 卷积核数量
        pool_size=2,  # 池化区域大小
        pool_stride=2,  # 池化步长
        act="relu")  # 激活函数
    drop = fluid.layers.dropout(x=conv_pool_1,  # 输入
                                dropout_prob=0.5)  # 丢弃率

    # 第二组 卷积池化+dropout
    conv_pool_2 = fluid.nets.simple_img_conv_pool(
        input=drop,  # 输入：上一层输出作为输入
        filter_size=3,  # 卷积核大小
        num_filters=64,  # 卷积核数量
        pool_size=2,  # 池化区域大小
        pool_stride=2,  # 池化步长
        act="relu")  # 激活函数
    drop = fluid.layers.dropout(x=conv_pool_2,  # 输入
                                dropout_prob=0.5)  # 丢弃率

    # 第三组 卷积池化+dropout
    conv_pool_3 = fluid.nets.simple_img_conv_pool(
        input=drop,  # 输入：上一层输出作为输入
        filter_size=3,  # 卷积核大小
        num_filters=64,  # 卷积核数量
        pool_size=2,  # 池化区域大小
        pool_stride=2,  # 池化步长
        act="relu")  # 激活函数
    drop = fluid.layers.dropout(x=conv_pool_3,  # 输入
                                dropout_prob=0.5)  # 丢弃率
    # 第一层fc
    fc = fluid.layers.fc(input=drop,  # 输入
                         size=512,  # 神经元数量（经验值）
                         act="relu")  # 激活函数
    drop = fluid.layers.dropout(x=fc, dropout_prob=0.5)
    # 输出层
    predict = fluid.layers.fc(input=drop,  # 输入
                              size=type_size,  # 神经元数量
                              act="softmax")  # 输出层采用softmax
    return predict


# 定义reader
BATCH_SIZE = 32  # 批次大小
train_reader = train_r(train_file_path)  # 训练集reader
random_train_reader = paddle.reader.shuffle(train_reader,
                                            buf_size=1300)
batch_train_reader = paddle.batch(random_train_reader,
                                  batch_size=BATCH_SIZE)

# 张量占位符
image = fluid.layers.data(name="image",  # 名称
                          shape=[3, 128, 128],  # 形状
                          dtype="float32")  # 类型
label = fluid.layers.data(name="label",
                          shape=[1],
                          dtype="int64")  # 标签值为整数

predict = create_CNN(image, type_size=5)

# 损失函数
cost = fluid.layers.cross_entropy(input=predict,  # 预测值
                                  label=label)  # 真实值
avg_cost = fluid.layers.mean(cost)

# 优化器
optimizer = fluid.optimizer.Adam(learning_rate=0.001)
optimizer.minimize(avg_cost)  # 指定优化器目标函数

# accuracy
accuracy = fluid.layers.accuracy(input=predict,  # 预测值
                                 label=label)  # 真实值

# 执行器
place = fluid.CUDAPlace(0) # GPU，0表示第一个GPU
exe = fluid.Executor(place) # 执行器
exe.run(fluid.default_startup_program()) # 初始化

# feeder
feeder = fluid.DataFeeder(feed_list=[image, label],
                          place=place)

costs = [] # 记录损失值
accs = [] # 记录正确率
times = 0 # 计数器
batches = [] # 记录迭代次数

# 训练
for epoch in range(120): # 外层循环控制轮次
    for batch_id, data in enumerate(batch_train_reader()):
        times += 1
        c, a = exe.run(fluid.default_main_program(),
                       feed=feeder.feed(data),
                       fetch_list=[avg_cost, accuracy])
        if batch_id % 20 ==0 : # 每20批次打印一笔
            print("epoch:%d, batch:%d, cost:%f, acc:%f" %
                  (epoch, batch_id, c[0], a[0]))
            accs.append(a[0]) # 准确率记录到列表
            costs.append(c[0]) # 损失值记录到列表
            batches.append(times) # 迭代批次记录到列表
print("训练结束.")

# 训练结束后，保存推理模型
model_save_dir = "model/"
if not os.path.exists(model_save_dir): # 目录不存在
    os.makedirs(model_save_dir)

fluid.io.save_inference_model(model_save_dir,#保存目录
                              ["image"],#预测时输入的张量名称
                              [predict],#预测结果从哪里获取
                              exe)#执行器
print("保存推理模型成功.")

# 训练过程可视化
plt.title("trainning")
plt.xlabel("iter")
plt.ylabel("cost/acc")
plt.plot(batches, costs, color="red", label="cost")
plt.plot(batches, accs, color="blue", label="accuracy")
plt.legend()
plt.grid()
plt.savefig("train.png")
plt.show()


####################### 测试 #######################
from PIL import Image

# 读取测试图像
def load_img(path):
    # 读取图像，并缩放、裁剪
    img = paddle.dataset.image.load_and_transform(
        path, # 测试图片路径
        128, 128,# 缩放、裁剪大小(测试和训练保持一致)
        False) # 测试模型
    # 归一化
    img = img.astype("float32") / 255.0

    return img

# 加载模型
place = fluid.CPUPlace() # 推理在CPU上执行
infer_exe = fluid.Executor(place) # 用于推理的执行器
model_save_dir = "model/" # 模型保存目录

infer_prog, feed_vars, fetch_targets = \
    fluid.io.load_inference_model(model_save_dir, infer_exe)

test_img = "apple_1.png" # 测试图片路径
infer_imgs = [] # 待预测图像数据

infer_imgs.append(load_img(test_img)) # 读取图像，存入列表
infer_imgs = numpy.array(infer_imgs) # 转数组(数组和张量类型兼容)
params = {feed_vars[0]:infer_imgs} # 参数字典

results = infer_exe.run(infer_prog, # 推理的Program
                        feed=params,# 喂入待预测图像数据
                        fetch_list=fetch_targets)#返回结果

idx = numpy.argmax(results[0][0]) # 返回预测概率最高的索引
for k, v in name_dict.items(): # 遍历名称-编号字典
    if idx == v: # 概率最高的索引等于类别编号
        print("预测结果:", k)

# 显示测试图像
img = Image.open(test_img)
plt.imshow(img)
plt.show()





