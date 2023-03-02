'''读取图像，保存图像,显示图像'''
import cv2

#读取图像
img = cv2.imread('../data/Linus.png')
# print(type(img))
# print(img.shape) #高度，宽度，通道数

cv2.imshow('img',img)
cv2.imshow('img1',img)

#保存图像
cv2.imwrite('./newimg.jpg',img)

cv2.waitKey() #进入阻塞等待状态，等待用户按下每个按键
cv2.destroyAllWindows()





