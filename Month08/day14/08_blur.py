'''
图像的模糊：减少像素与像素之间的差异
均值滤波、高斯滤波、中值滤波
'''
import cv2
import numpy as np

img = cv2.imread('../data/salt.jpg')
cv2.imshow('img', img)
# 均值滤波
mean = cv2.blur(img, (5, 5))
cv2.imshow('mean', mean)
# 高斯滤波
gaussian = cv2.GaussianBlur(img, (5, 5), 3)
cv2.imshow('gaussian', gaussian)
# 中值滤波
median = cv2.medianBlur(img, 5)
cv2.imshow('median', median)

# 自定义卷积核实现卷积
filter_w = np.ones((5, 5), dtype='float32') / 25.0
res = cv2.filter2D(img,
                   -1,  # 与原始图像一致
                   filter_w)
cv2.imshow('res',res)

cv2.waitKey()
cv2.destroyAllWindows()
