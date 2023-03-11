# 01_tile_sample_enhance.py
# 瓷砖数据增强
import cv2
import numpy as np
from global_var import *
import os
from math import *

# 不切边旋转
def remote(img, angle):
    h, w = img.shape[:2]
    h_new = int(w * fabs(sin(radians(angle))) + h * fabs(cos(radians(angle))))
    w_new = int(h * fabs(sin(radians(angle))) + w * fabs(cos(radians(angle))))

    matRotation = cv2.getRotationMatrix2D((w / 2, h / 2), angle, 1)

    matRotation[0, 2] += (w_new - w) / 2
    matRotation[1, 2] += (h_new - h) / 2

    imgRotation = cv2.warpAffine(img, matRotation, (w_new, h_new), borderValue=(255, 255, 255))

    return imgRotation

def rotate(img, angle, center=None, scale=1.0):
    """
    图像旋转变换
    :param img: 原始图像数据
    :param angle: 旋转角度
    :param center: 旋转中心，如果为None则以原图中心为旋转中心
    :param scale: 缩放比例，默认为1
    :return: 返回旋转后的图像
    """
    h, w = img.shape[:2]  # 获取图像高、宽

    # 旋转中心默认为图像中心
    if center is None:
        center = (w / 2, h / 2)

    # 计算旋转矩阵
    M = cv2.getRotationMatrix2D(center, angle, scale)

    # 使用openCV仿射变换实现函数旋转
    rotated = cv2.warpAffine(img, M, (w, h))

    return rotated  # 返回旋转后的矩阵

def rotate_all(): # 旋转增强
    dirs = os.listdir(data_root) # 列出所有子目录
    for d in dirs:
        sub_dir = os.path.join(data_root, d) # 拼完整路径
        if not os.path.isdir(sub_dir): # 不是目录
            continue

        img_dir_path = os.path.join(sub_dir, "Imgs")#Imgs子目录
        imgs = os.listdir(img_dir_path) # 列出所有图片
        for fn in imgs: # 遍历每个图片文件
            img_full_path = os.path.join(img_dir_path, fn)
            # 取出原图片文件名、后缀名部分，拼接新图像名称
            pos = fn.find(".") # 返回.的位置
            name = fn[0:pos] # 名称部分
            suffix = fn[pos:] # 后缀名部分

            im = cv2.imread(img_full_path) # 读取图像

            for i in range(1, 8):
                img_new = remote(im, i * 45) # 不切边旋转
                # 拼接新文件名称、路径
                new_name = "%s_rotate_%d%s" %(name, i, suffix)
                new_img_path = os.path.join(img_dir_path, new_name)
                # 保存
                cv2.imwrite(new_img_path, img_new)
                print("Save OK:", new_img_path)


if __name__ == "__main__":
    rotate_all() # 旋转增强

    # 可以单独加一些增强策略，对数量较少的类别单独做增强处理

    print("数据增强处理结束.")
