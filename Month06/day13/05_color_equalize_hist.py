'''
彩色图像，亮度直方图均衡化
'''
import cv2

#BGR
img = cv2.imread('../data/sunrise.jpg')
cv2.imshow('img',img)
#BGR --> HSV
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

hsv[...,-1] = cv2.equalizeHist(hsv[...,-1])

# HSV --> BGR
res = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.imshow('res',res)

cv2.waitKey()
cv2.destroyAllWindows()