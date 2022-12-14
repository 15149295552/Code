'''
轮廓的拟合，拟合多边形
精度越大，精度越低，  精度越小，精度越高
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
# 精度1
adp1 = img.copy()
eps = 0.005 * cv2.arcLength(cnts[0],True) #周长
points = cv2.approxPolyDP(cnts[0],eps,True)
adp1 = cv2.drawContours(adp1,[points],-1,(0,0,255),2)
cv2.imshow('res_0.005',adp1)

# 精度2
adp2 = img.copy()
eps = 0.01 * cv2.arcLength(cnts[0],True) #周长
points = cv2.approxPolyDP(cnts[0],eps,True)
adp2 = cv2.drawContours(adp2,[points],-1,(0,0,255),2)
cv2.imshow('res_0.01',adp2)


cv2.waitKey()
cv2.destroyAllWindows()
