'''图像的翻转（镜像）'''
import cv2

img = cv2.imread('../data/Linus.png')
cv2.imshow('img',img)
#垂直镜像
flip0 = cv2.flip(img,0)
cv2.imshow('flip0',flip0)
#水平镜像
flip1 = cv2.flip(img,1)
cv2.imshow('flip1',flip1)


cv2.waitKey()
cv2.destroyAllWindows()