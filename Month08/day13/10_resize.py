'''
图像的放大和缩小
'''
import cv2

img = cv2.imread('../data/Linus.png')
cv2.imshow('img',img)

h,w = img.shape[:2]
#缩小
dst_size = (int(w/2),int(h/2))
res = cv2.resize(img,dst_size)
cv2.imshow('res',res)

#放大
dst_size = (w*2,h*2)
#最邻近插值法
nearest = cv2.resize(img,
                     dst_size,
                     interpolation=cv2.INTER_NEAREST)
cv2.imshow('nearest',nearest)
#双线性插值法
linear = cv2.resize(img,
                    dst_size,
                    interpolation=cv2.INTER_LINEAR)
cv2.imshow('linear',linear)


cv2.waitKey()
cv2.destroyAllWindows()
