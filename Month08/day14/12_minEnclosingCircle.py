'''
拟合轮廓的最小包围圆
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
center,radius = cv2.minEnclosingCircle(cnts[0])
# print('圆心:{},半径:{}'.format(center,radius))
center = (int(center[0]),int(center[1]))
radius = int(radius)

cv2.circle(img,center,radius,(0,0,255),2)
cv2.imshow('res',img)

cv2.waitKey()
cv2.destroyAllWindows()
