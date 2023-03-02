'''
图像的相加:对应位置像素值对应相加(两张图像尺寸要一致)
'''
import cv2

lena = cv2.imread('../data/lena.jpg',0)
lily = cv2.imread('../data/lily_square.png',0)
cv2.imshow('lena',lena)
cv2.imshow('lily',lily)
#相加
add = cv2.add(lena,lily)
cv2.imshow('add',add)
#按照权重进行相加
res = cv2.addWeighted(lena,0.2,
                      lily,0.8,
                      0)#亮度调节量
cv2.imshow('res',res)

cv2.waitKey()
cv2.destroyAllWindows()