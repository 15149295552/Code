'''
彩色图像转为灰度图像
转换色彩空间  默认的色彩空间:BGR    [255,6,89]
灰度图像不能转为彩色图像】
----
当在你的任务需求中，根本用不到彩色图像，直接使用flags=0读取灰度图像
当在你的任务需求中，需要用到彩色图像，读取彩色，将彩色转为灰度
'''
import cv2

img = cv2.imread('../data/lena.jpg',1) #1:彩色  0：灰度
cv2.imshow('img',img)
#转换色彩空间BGR --- > GRAY
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)


cv2.waitKey()
cv2.destroyAllWindows()
