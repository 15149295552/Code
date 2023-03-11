# 人脸(水果)识别示例：预测
import paddle
import paddle.fluid as fluid
import numpy as np
import sys
import os
import matplotlib.pyplot as plt
from PIL import Image
from .global_var import *
# from .sample_pre_handle import *

img_size = 200  # 训练图像大小

place = None
exe = None
infer_program, feed_names, fetch_targets = None, None, None


# 加载模型
def core_load_freeze_models():
    print("core_load_freeze_models()")

    global place
    global exe
    global infer_program, feed_names, fetch_targets

    # 执行器
    place = fluid.CPUPlace()
    exe = fluid.Executor(place)
    infer_program, feed_names, fetch_targets = fluid.io.load_inference_model(freeze_model_dir,
                                                                             exe)
    print("完成模型加载")


# 加载数据
def core_load_image(path):
    img = paddle.dataset.image.load_and_transform(path, img_size, img_size, False).astype("float32")
    img = img / 255.0
    return img


# 单张图像预测预测
def core_do_infer(img):
    global place
    global exe
    global infer_program, feed_names, fetch_targets

    infer_imgs = []  # 待预测列表

    infer_imgs.append(img)
    # print("type(img):", type(img))
    infer_imgs = np.array(infer_imgs)

    # 开始预测
    results = exe.run(infer_program,
                      feed={feed_names[0]: infer_imgs},
                      fetch_list=fetch_targets)
    print("result:\n", results)

    return results[0][0]
