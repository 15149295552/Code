'''开运算:先腐蚀，在膨胀'''
import cv2
import numpy as np

img = cv2.imread('../data/5.png')
cv2.imshow('img',img)

kernel = np.ones((3,3),np.uint8)
res = cv2.morphologyEx(img,
                       cv2.MORPH_OPEN,
                       kernel,
                       iterations=8)
cv2.imshow('res',res)


cv2.waitKey()
cv2.destroyAllWindows()