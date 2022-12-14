'''
形态学梯度：膨胀 - 腐蚀
'''
import cv2
import numpy as np

img = cv2.imread('../data/6.png')
cv2.imshow('img',img)
#形态学梯度
kernel = np.ones((2,2),np.uint8)
res = cv2.morphologyEx(img,
                       cv2.MORPH_GRADIENT,
                       kernel)
cv2.imshow('res',res)

cv2.waitKey()
cv2.destroyAllWindows()


