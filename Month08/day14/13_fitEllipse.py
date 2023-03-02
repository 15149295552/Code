'''
拟合轮廓的椭圆
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
params = cv2.fitEllipse(cnts[0])

cv2.ellipse(img,params,color=(0,0,255),thickness=2)
cv2.imshow('res',img)

cv2.waitKey()
cv2.destroyAllWindows()
