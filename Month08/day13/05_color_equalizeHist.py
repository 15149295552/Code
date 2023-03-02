'''
彩色图像直方图均衡化（亮度）
'''
import cv2

img = cv2.imread('../data/sunrise.jpg')#BGR
cv2.imshow('img',img)
#BGR-->HSV
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hsv[..., 2] = cv2.equalizeHist(hsv[...,2])
#HSV-->BGR
res = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.imshow('res',res)

cv2.waitKey()
cv2.destroyAllWindows()