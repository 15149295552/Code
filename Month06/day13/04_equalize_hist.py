'''
灰度图像的直方图均衡化
'''
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../data/sunrise.jpg',0)
cv2.imshow('img',img)
#直方图均衡化
res = cv2.equalizeHist(img)
cv2.imshow('res',res)

#显示原始图像的直方图
plt.subplot(2,1,1)
plt.hist(img.ravel(),
         bins=256,
         range=[0,256])
#显示均衡化之后的直方图
plt.subplot(2,1,2)
plt.hist(res.ravel(),
         bins=256,
         range=[0,256])

plt.show()

cv2.waitKey()
cv2.destroyAllWindows()



