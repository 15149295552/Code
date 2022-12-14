'''
图像相加：两张图像尺寸必须一致，对应位置像素值，对应相加
'''

import cv2

lena = cv2.imread('../data/lena.jpg',0)
lily = cv2.imread('../data/lily_square.png',0)

cv2.imshow('lena',lena)
cv2.imshow('lily',lily)
#add
res = cv2.add(lena,lily)
cv2.imshow('res',res)

#addWeighted
dst2 = cv2.addWeighted(lena,0.2,
                       lily,0.8,
                       50)#亮度调节量
cv2.imshow('dst2',dst2)


cv2.waitKey()
cv2.destroyAllWindows()


