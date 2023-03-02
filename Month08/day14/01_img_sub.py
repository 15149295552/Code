'''图像相减
   找到两幅图像的差异'''
import cv2

img3 = cv2.imread('../data/3.png',0)
img4 = cv2.imread('../data/4.png',0)
cv2.imshow('img3',img3)
cv2.imshow('img4',img4)
#减法
sub = cv2.subtract(img3,img4)
cv2.imshow('sub',sub)


cv2.waitKey()
cv2.destroyAllWindows()






