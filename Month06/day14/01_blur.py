'''
图像的模糊：缩小像素与像素之间的差异值
'''
import cv2
import numpy as np

img = cv2.imread('../data/salt.jpg')
cv2.imshow('img',img)

#均值滤波
mean = cv2.blur(img,(5,5))
cv2.imshow('mean',mean)
#高斯滤波
gaussian = cv2.GaussianBlur(img,(5,5),3)
cv2.imshow('gaussian',gaussian)
#中值滤波
median = cv2.medianBlur(img,5)
cv2.imshow('median',median)
cv2.imwrite('res.jpg',median)

#自定义均值滤波卷积核，进行卷积
mean_filter = np.array([[1,1,1],
                        [1,1,1],
                        [1,1,1]],np.float32) / 9.0
res = cv2.filter2D(img,
                   -1, #图像深度，元素类型，-1代表和原始图像一致
                   mean_filter)
cv2.imshow('res',res)



cv2.waitKey()
cv2.destroyAllWindows()