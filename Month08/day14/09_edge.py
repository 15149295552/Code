'''
边沿检测
'''
import cv2

img = cv2.imread('../data/lily.png',0)
cv2.imshow('img',img)
#Sobel
sobel = cv2.Sobel(img,
                  cv2.CV_64F,#图像的深度
                  dx=1,dy=1,#水平和垂直方向的滤波计算
                  ksize=5)#滤波器大小
cv2.imshow('sobel',sobel)
#Laplacain
lap = cv2.Laplacian(img,cv2.CV_64F,ksize=5)
cv2.imshow('lap',lap)
#Canny
canny = cv2.Canny(img,
                  70,
                  300)
cv2.imshow('canny',canny)



cv2.waitKey()
cv2.destroyAllWindows()





