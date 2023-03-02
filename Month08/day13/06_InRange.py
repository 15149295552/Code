'''
通过inrange函数，提取指定的颜色
H   蓝色：120  绿色：60 红色：0
'''
import cv2
import numpy as np

img = cv2.imread('../data/opencv2.png')
cv2.imshow('img',img)
#BGR-->HSV
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
min_val = np.array([0,50,50])
max_val = np.array([10,255,255])
mask = cv2.inRange(hsv,min_val,max_val)
cv2.imshow('mask',mask)
#原始图像和原始图像做位与
res = cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('res',res)

cv2.waitKey()
cv2.destroyAllWindows()