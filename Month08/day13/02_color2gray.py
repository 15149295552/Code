'''
彩色图像转为灰度图像(不可逆)
转换色彩空间 彩色：BGR   灰度：GRAY
'''
import cv2
#读取彩色图像
img = cv2.imread('../data/lena.jpg') #1:彩色 0：灰度
cv2.imshow('img',img)
#将彩色图像转为灰度图像  BGR--->GRAY
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)

cv2.waitKey()
cv2.destroyAllWindows()