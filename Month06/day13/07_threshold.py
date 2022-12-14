'''
二值化与反二值化
'''
import cv2

img = cv2.imread('../data/CPU3.png',0)
cv2.imshow('img',img)
#二值化
t,binary = cv2.threshold(img,#待处理图像
                         160,#阈值
                         255,#大于阈值转成的值
                         cv2.THRESH_BINARY)#二值化
cv2.imshow('res',binary)



cv2.waitKey()
cv2.destroyAllWindows()