'''
图像的缩放：放大和缩小
'''
import cv2

img = cv2.imread('../data/Linus.png')
cv2.imshow('img',img)

h,w = img.shape[:2]
#缩小
dsize = (int(w/2),int(h/2))
reduce = cv2.resize(img,dsize)
cv2.imshow('reduce',reduce)

#放大
dsize = (w*2,h*2)
nearest = cv2.resize(img,dsize,
                     interpolation=cv2.INTER_NEAREST)
cv2.imshow('nearest',nearest)

#双线性插值法
linear = cv2.resize(img,dsize,
                    interpolation=cv2.INTER_LINEAR)
cv2.imshow('linear',linear)

cv2.waitKey()
cv2.destroyAllWindows()
