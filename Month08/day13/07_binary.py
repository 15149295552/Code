'''
二值化与反二值化
'''
import cv2

img = cv2.imread('../data/CPU3.png')
cv2.imshow('img',img)
#灰度化
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',gray)
#二值化
t,binary = cv2.threshold(gray,
                         155,
                         255,
                         cv2.THRESH_BINARY_INV)
cv2.imshow('binary',binary)

cv2.waitKey()
cv2.destroyAllWindows()




