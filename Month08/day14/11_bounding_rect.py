'''
拟合轮廓的外接矩形
'''
import cv2
import numpy as np

img = cv2.imread('../data/cloud.png')
cv2.imshow('img', img)
# 灰度化
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 二值化
t, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
cv2.imshow('binary', binary)
# 查找轮廓
cnts, hie = cv2.findContours(binary,
                             cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_NONE)

# 根据轮廓坐标点生成拟合轮廓的参数
x, y, w, h = cv2.boundingRect(cnts[0])

points = np.array([[[x, y]],  # 左上角
                   [[x, y + h]],  # 左下角
                   [[x + w, y + h]],  # 右下角
                   [[x + w, y]]])  # 右上角

res = cv2.drawContours(img,[points],0,(0,0,255),2)
cv2.imshow('res',res)

cv2.waitKey()
cv2.destroyAllWindows()
