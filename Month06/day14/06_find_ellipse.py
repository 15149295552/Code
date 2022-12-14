'''
轮廓的拟合，拟合椭圆
'''
import cv2
import numpy as np

img = cv2.imread('../data/cloud.png')
cv2.imshow('img',img)
#灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
t,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow('binary',binary)

#查找轮廓
cnts,hie = cv2.findContours(binary,
                            cv2.RETR_EXTERNAL,#只检测外层轮廓
                            cv2.CHAIN_APPROX_NONE)#保存所有坐标点
# print(len(cnts))

#根据轮廓坐标，生成拟合轮廓信息
params = cv2.fitEllipse(cnts[0])

res = cv2.ellipse(img,params,(0,0,255),2)
cv2.imshow('res',res)

cv2.waitKey()
cv2.destroyAllWindows()
