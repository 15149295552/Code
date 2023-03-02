'''
度盘区域的瑕疵检测
'''
import cv2
import numpy as np

# 1.读取图像
img = cv2.imread('../data/CPU3.png')
# cv2.imshow('img',img)
# 2.灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray',gray)
# 3.二值化
t,binary = cv2.threshold(gray,155,255,cv2.THRESH_BINARY)
# cv2.imshow('binary',binary)
# 4.查找度盘区域的轮廓
cnts,hie = cv2.findContours(binary,
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_NONE)
# print(len(cnts))
# 5.做出来一个全黑色的图像mask(shape=二值化的图像)
mask = np.zeros_like(binary)
# cv2.imshow('mask',mask)
# 6.将度盘的轮廓使用石新华填充画在mask
img_fill = cv2.drawContours(mask,cnts,-1,255,-1)
# cv2.imshow('img_fill',img_fill)
# 7.将mask与二值化做减法，得到瑕疵区域
img_sub = cv2.subtract(img_fill,binary)
# cv2.imshow('img_sub',img_sub)
# 8.将瑕疵做闭运算，收缩离散点
close = cv2.morphologyEx(img_sub,cv2.MORPH_CLOSE,(3,3),
                         iterations=3)
# cv2.imshow('close',close)
# 9.计算瑕疵的面积  (行业标准：18)
cnts,hie = cv2.findContours(close,
                            cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_NONE)
#根据面积进行排序，拿到面积最大的瑕疵轮廓
cnts = sorted(cnts,key=cv2.contourArea,reverse=True)
dst_cnt = cnts[0]#目标瑕疵轮廓
area = cv2.contourArea(dst_cnt)
if area > 18:
    #如果瑕疵面积大于行业标准，拟合瑕疵的外接圆
    center,radius = cv2.minEnclosingCircle(dst_cnt)
    center = (int(center[0]),int(center[1]))
    radius = int(radius)
    #将外接圆画在原始图像上
    res = cv2.circle(img,center,radius,(0,0,255),2)
    print('当前图像有瑕疵,瑕疵面积为:',area)
    cv2.imshow('res',res)
    cv2.imwrite('res.png',res)
else:
    print('好！！！！')

cv2.waitKey()
cv2.destroyAllWindows()