'''
查找并绘制轮廓
'''
import cv2

img = cv2.imread('../data/3.png')
cv2.imshow('img',img)
#将彩色图像转为灰度图像
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#二值化
t,binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
cv2.imshow('binary',binary)

#查找轮廓
cnts,hie = cv2.findContours(binary,
                            cv2.RETR_EXTERNAL,#只检测外层轮廓
                            cv2.CHAIN_APPROX_NONE)#保存所有坐标点
# print(type(cnts))
# # for cnt in cnts:
# #     print(cnt.shape)
# # print(hie)

#绘制轮廓
res = cv2.drawContours(img,#在那张图像上画轮廓
                       cnts,#轮廓坐标，列表套三维数组
                       -1,#轮廓索引，-1为所有
                       (0,0,255),#轮廓颜色，BGR
                       2)#线条粗细  2px   -1则为实心化填充
cv2.imshow('res',res)


cv2.waitKey()
cv2.destroyAllWindows()
