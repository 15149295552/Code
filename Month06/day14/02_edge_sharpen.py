'''
图像锐化，边沿检测
'''
import cv2

img = cv2.imread('../data/lily.png',0)
cv2.imshow('img',img)
#Sobel
sobel = cv2.Sobel(img,
                  cv2.CV_64F,#图像的深度，元素类型
                  dx=1,dy=1, #水平，垂直方向滤波计算
                  ksize=5)
cv2.imshow('sobel',sobel)
#Lap
lap = cv2.Laplacian(img,
                    cv2.CV_64F,
                    ksize=5)
cv2.imshow('lap',lap)

#Canny
canny = cv2.Canny(img,
                  50,#滞后阈值
                  300)#模糊度
cv2.imshow('canny',canny)



cv2.waitKey()
cv2.destroyAllWindows()



