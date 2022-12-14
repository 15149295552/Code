'''
透视变换
'''

import cv2
import numpy as np

img = cv2.imread('../data/pers.png')
cv2.imshow('img',img)

#透视变换
h,w = img.shape[:2]
#透视变换矩阵
pts1 = np.float32([[58, 2], [167, 9], [8, 196], [126, 196]])# 输入图像四个顶点坐标
pts2 = np.float32([[16, 2], [167, 8], [8, 196], [169, 196]])# 输出图像四个顶点坐标
M = cv2.getPerspectiveTransform(pts1,pts2)

res = cv2.warpPerspective(img,
                          M,
                          (w,h))
cv2.imshow('res',res)


cv2.waitKey()
cv2.destroyAllWindows()

#休息15分钟， 17:20回来





