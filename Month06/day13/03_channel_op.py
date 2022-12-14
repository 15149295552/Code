'''
对于某个图像的通道操作
'''
import cv2

img = cv2.imread('../data/opencv2.png')
cv2.imshow('img',img)

#取出蓝色通道，并显示
b = img[:,:,0]
cv2.imshow('b',b)

#将蓝色通道取出，赋值为0
img[:,:,0] = 0
cv2.imshow('img-b0',img)

#将蓝色通道置0的基础上，再将绿色通道置0
img[:,:,1] = 0
cv2.imshow('img-b0-g0',img)


cv2.waitKey()
cv2.destroyAllWindows()