# 01_capsules_detection.py
# 利用图像实现胶囊瑕疵检测
import cv2
import numpy as np
import os


# 判断是否有气泡
def bub_detection(img_path, fn, im, im_gray):
    # 模糊
    im_blur = cv2.GaussianBlur(im_gray, (3, 3), 0)
    # Canny边沿提取
    im_canny = cv2.Canny(im_blur, 60, 240)
    cv2.imshow("im_canny", im_canny)
    # 轮廓查找
    # cnts, hie = cv2.findContours(im_canny,  # Opencv4.x
    img, cnts, hie = cv2.findContours(im_canny,  # Opencv3.x
                                      cv2.RETR_CCOMP,
                                      cv2.CHAIN_APPROX_NONE)

    new_cnts = [] # 过滤后的轮廓
    for i in range(len(cnts)):
        area = cv2.contourArea(cnts[i]) # 计算面积
        cir_len = cv2.arcLength(cnts[i], True) # 计算周长

        if area >= 10000 or cir_len >= 1000 or area < 5: # 过滤过大、过小的轮廓
            continue

        if hie[0][i][3] != -1: # 当前轮廓存在父轮廓(内部轮廓，保留)
            new_cnts.append(cnts[i])

    # 绘制轮廓
    im_cnt = cv2.drawContours(im,  # 在三通道图像上绘制
                              new_cnts,  # 绘制过滤后的轮廓
                              -1,  # 绘制所有轮廓
                              (0, 0, 255), 2)  # 颜色、粗细
    cv2.imshow("im_cnt", im_cnt)

    if len(new_cnts) > 0: # 经过过滤后的轮廓数量大于0
        print("气泡或黑点:", fn)
        new_path = "capsules/bub/" + fn  # 新路径
        os.rename(img_path, new_path)  # 移动文件
        print("移动文件成功:%s ===> %s" % (img_path, new_path))
        return True
    else:
        return False


# 判断是否为空胶囊
def empty_detection(img_path, fn, im, im_gray):
    # 模糊处理，合并细节
    im_blur = cv2.GaussianBlur(im_gray, (3, 3), 0)
    cv2.imshow("im_blur", im_blur)
    # 二值化
    t, im_bin = cv2.threshold(im_blur, 210, 255, cv2.THRESH_BINARY)
    cv2.imshow("im_bin", im_bin)
    # 轮廓查找
    # cnts, hie = cv2.findContours(im_bin,  # Opencv4.x
    img, cnts, hie = cv2.findContours(im_bin,  # Opencv3.x
                                      cv2.RETR_CCOMP,
                                      cv2.CHAIN_APPROX_NONE)
    # 根据周长过滤
    new_cnts = []  # 过滤后的轮廓
    for i in range(len(cnts)):
        cir_len = cv2.arcLength(cnts[i], True)  # 计算轮廓周长
        if cir_len >= 1000:  # 周长超过1000
            new_cnts.append(cnts[i])

    # 绘制轮廓
    im_cnt = cv2.drawContours(im,  # 在三通道图像上绘制
                              new_cnts,  # 绘制过滤后的轮廓
                              -1,  # 绘制所有轮廓
                              (0, 0, 255), 2)  # 颜色、粗细
    cv2.imshow("im_cnt", im_cnt)

    if len(new_cnts) == 1:  # 只有一个轮廓, 空胶囊
        print("空胶囊:", fn)
        new_path = "capsules/empty/" + fn  # 新路径
        os.rename(img_path, new_path)  # 移动文件
        print("移动文件成功:%s ===> %s" % (img_path, new_path))
        return True
    else:
        return False


if __name__ == "__main__":
    img_dir = "./capsules/"  # 图片所在的目录
    img_files = os.listdir(img_dir)  # 列出目录下所有图片

    for fn in img_files:  # 遍历
        img_path = img_dir + fn  # 文件完整路径

        if os.path.isdir(img_path):  # 目录
            continue

        im = cv2.imread(img_path)  # 读取图片内容
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # 转灰度图像
        cv2.imshow("im", im)
        cv2.imshow("im_gray", im_gray)

        # 空胶囊判断
        is_empty = False
        # is_empty = empty_detection(img_path, fn, im, im_gray)

        # 气泡检测
        is_bub = False
        if not is_empty:  # 等价于if is_empty == False
            is_bub = bub_detection(img_path, fn, im, im_gray)

        cv2.waitKey()
        cv2.destroyAllWindows()
