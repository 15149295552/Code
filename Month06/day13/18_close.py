'''
闭运算： 先膨胀，在腐蚀
'''
import cv2
import numpy as np

img = cv2.imread('../data/9.png')
cv2.imshow('img',img)

kernel = np.ones((2,2),np.uint8)
res = cv2.morphologyEx(img,
                       cv2.MORPH_CLOSE,
                       kernel,
                       iterations=8)
cv2.imshow('res',res)


cv2.waitKey()
cv2.destroyAllWindows()