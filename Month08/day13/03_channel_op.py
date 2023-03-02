'''
对图像的某个通道进行操作
'''
import cv2

img = cv2.imread('../data/opencv2.png')
cv2.imshow('img',img)
#在原始图像中，单独取到蓝色通道，并显示
b = img[:,:,0]
cv2.imshow('b',b)
#在原始图像上，将蓝色通道置0
img[:,:,0] = 0
cv2.imshow('b0',img)
#在蓝色置0的基础上，再将绿色置0
img[:,:,1] = 0
cv2.imshow('b0g0',img)

cv2.waitKey()
cv2.destroyAllWindows()