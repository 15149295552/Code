'''
通过inRange函数，提取指定的颜色
H中的相位角： 蓝色为120   绿色为60  红色为0
'''
import cv2
import numpy as np

img = cv2.imread('../data/opencv2.png')
cv2.imshow('img',img)
#BGR ---> HSV
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
#提取蓝色部分
minVal = np.array([110,50,50])
maxVal = np.array([130,255,255])
#提取范围
mask = cv2.inRange(hsv,minVal,maxVal)
cv2.imshow('mask',mask)
#让原始图像和原始图像做位与
res = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('res',res)

cv2.waitKey()
cv2.destroyAllWindows()