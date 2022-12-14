'''
镜像（翻转）
'''
import cv2

img = cv2.imread('../data/Linus.png')
cv2.imshow('img',img)
#垂直镜像
res0 = cv2.flip(img,0)
cv2.imshow('res0',res0)
#水平镜像
res1 = cv2.flip(img,1)
cv2.imshow('res1',res1)

cv2.waitKey()
cv2.destroyAllWindows()

