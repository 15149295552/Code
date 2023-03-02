'''
拟合轮廓的多边形
精度一般采用周长的XX倍
精度值越大，精度越低。精度值越小，精度越高
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
adp1 = img.copy()
eps = 0.005 * cv2.arcLength(cnts[0],True)
approx = cv2.approxPolyDP(cnts[0],eps,True)
cv2.drawContours(adp1,[approx],0,(0,0,255),2)
cv2.imshow('adp1',adp1)

adp2 = img.copy()
eps = 0.01 * cv2.arcLength(cnts[0],True)
approx = cv2.approxPolyDP(cnts[0],eps,True)
cv2.drawContours(adp2,[approx],0,(0,0,255),2)
cv2.imshow('adp2',adp2)

cv2.waitKey()
cv2.destroyAllWindows()
