'''
集成电路，瑕疵检测
'''
import cv2
import numpy as np

# 1.读取原始图像
img = cv2.imread('../data/CPU3.png')
cv2.imshow('img',img)
# 2.灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
# 3.二值化   阈值：162
t,binary = cv2.threshold(gray,162,255,cv2.THRESH_BINARY)
cv2.imshow('binary',binary)
# 4.在二值图上，提取轮廓（提取外层轮廓）
cnts,hie = cv2.findContours(binary,
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_NONE)
# print(len(cnts))
# 5.生成mask图像，shape等同于二值图，并且使用0填充
mask = np.zeros(binary.shape,np.uint8)
# 6.将查找到的轮廓，使用实心化填充，填充在mask上
img_fill = cv2.drawContours(mask,cnts,-1,255,-1)
cv2.imshow('img_fill',img_fill)
# 7.使用填充后的图像，减去二值图，得到瑕疵区域
img_sub = cv2.subtract(img_fill,binary)
cv2.imshow('img_sub',img_sub)
# 8.使用闭运算，将瑕疵区域的离散点进行收缩
kernel = np.ones((3,3),np.uint8)
img_close = cv2.morphologyEx(img_sub,cv2.MORPH_CLOSE,kernel)
cv2.imshow('close',img_close)
# 9.查找瑕疵区域的轮廓
cnts,hie = cv2.findContours(img_close,
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_NONE)
print(len(cnts))
# 10.拟合面积最大的瑕疵的最小外接圆
cnts = sorted(cnts,key=cv2.contourArea,reverse=True)
center,radius = cv2.minEnclosingCircle(cnts[0])
center = (int(center[0]),int(center[1]))
radius = int(radius)
# 11.将最小外接圆画在原始图上,
# 业务指标，面积大于10,则为瑕疵
area = cv2.contourArea(cnts[0])
if area > 10:
    print('瑕疵面积为:{},有瑕疵'.format(area))
    cv2.circle(img,center,radius,(0,0,255),2)
    cv2.imshow('res',img)
else:
    print('good产品')

cv2.waitKey()
cv2.destroyAllWindows()
