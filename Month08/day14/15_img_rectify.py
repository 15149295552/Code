'''
图像矫正：透视变换
'''
import cv2
import numpy as np
import math

img = cv2.imread('../data/paper.jpg')
cv2.imshow('img', img)
# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)

# 模糊
blured = cv2.GaussianBlur(gray, (5, 5), 0)
# 闭运算
close = cv2.morphologyEx(blured, cv2.MORPH_CLOSE, (3, 3))

# 边沿检测
# sobel = cv2.Sobel(gray,cv2.CV_64F,1,1,ksize=5)
# cv2.imshow('sobel',sobel)
# lap = cv2.Laplacian(gray,cv2.CV_64F,ksize=5)
# cv2.imshow('lap',lap)
canny = cv2.Canny(close, 30, 120)
cv2.imshow('canny', canny)

# 查找轮廓
cnts, hie = cv2.findContours(canny,
                             cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_SIMPLE)
# 找到所有轮廓中，面积最大的四边形
docCnt = None
if len(cnts) > 0:
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)
    for cnt in cnts:
        eps = 0.02 * cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, eps, True)
        # 拟合出来的第一个4边型，就是目标轮廓
        if len(approx) == 4:
            docCnt = approx
            break

img_copy = img.copy()

points = []
for peak in docCnt:
    peak = tuple(peak[0])
    points.append(peak)
    cv2.circle(img_copy, peak, 10, (0, 0, 255), 2)

# 左上角，左下角，右下角，右上角
points = np.array(points,dtype='float32')  # 变换之前的坐标点
cv2.imshow('img_copy', img_copy)
# 根据坐标点，计算目标轮廓的宽度和高度

h = int(math.sqrt((points[0][0] - points[1][0]) ** 2 + (points[0][1] - points[1][1]) ** 2))
w = int(math.sqrt((points[0][0] - points[3][0]) ** 2 + (points[0][1] - points[3][1]) ** 2))
#定义变换之后的坐标点
dst = np.float32([[0,0],[0,h],[w,h],[w,0]])
#构建透视变换的矩阵
M = cv2.getPerspectiveTransform(points,dst)
#执行透视变换
res = cv2.warpPerspective(img,M,(w,h))
cv2.imshow('res',res)

cv2.waitKey()
cv2.destroyAllWindows()







