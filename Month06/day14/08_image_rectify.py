'''
图像矫正
'''
import cv2
import numpy as np
import math

img = cv2.imread('../data/paper.jpg')
cv2.imshow('img', img)
# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
# 二值化(没有办法找到一个阈值，来分割背景和主体图像)
# t,binary = cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
# cv2.imshow('binary',binary)

# 模糊
blured = cv2.GaussianBlur(gray, (5, 5), 0)
# 闭运算
close = cv2.morphologyEx(blured, cv2.MORPH_CLOSE, (3, 3))

# 锐化（边沿检测）
canny = cv2.Canny(close, 30, 120)
cv2.imshow('canny', canny)

# 查找轮廓
cnts, hie = cv2.findContours(canny,
                             cv2.RETR_EXTERNAL,  # 只检测外层轮廓
                             cv2.CHAIN_APPROX_SIMPLE)  # 压缩坐标，终点坐标
# 绘制轮廓
img_copy = img.copy()
img_cnt = cv2.drawContours(img_copy, cnts, -1, (0, 0, 255), 2)
cv2.imshow('img_cnt', img_cnt)

# 在所有轮廓中，找到面积最大的四边形
docCnt = None #目标轮廓的四个角的顶点
if len(cnts) > 0:
    # 将轮廓按照面积进行降序排序  cv2.contourArea()
    cnts = sorted(cnts,
                  key=cv2.contourArea,
                  reverse=True)
    #遍历每一个轮廓，拟合轮廓的多边形
    for cnt in cnts:
        eps = 0.02 * cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,eps,True)
        #拟合出来的第一个四边形，就是目标轮廓
        if len(approx) == 4:
            docCnt = approx
            break
#绘制目标轮廓的四个角的顶点
points = []
for peak in docCnt:
    peak = tuple(peak[0]) #圆心
    #绘制角点
    cv2.circle(img_copy,peak,10,(0,0,255),2)
    points.append(peak)

cv2.imshow('img_point',img_copy)
#将points转换为二维数组:左上角，左下角，右下角，右上角
src = np.array(points,'float32')
#根据坐标点，求出纸的宽度和高度
h = int(math.sqrt((src[0][0] - src[1][0])**2 + (src[0][1] - src[1][1])**2))
w = int(math.sqrt((src[0][0] - src[3][0])**2 + (src[0][1] - src[3][1])**2))
#变换之后的点
dst = np.float32([[0,0],[0,h],[w,h],[w,0]])
#根据两组坐标，生成透视变换矩阵
M = cv2.getPerspectiveTransform(src,dst)
#执行透视变换
res = cv2.warpPerspective(img,
                          M,
                          (w,h))
cv2.imshow('res',res)

cv2.waitKey()
cv2.destroyAllWindows()


