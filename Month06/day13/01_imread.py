'''
利用opencv实现图像读取，显示，保存
'''

import cv2

#读取图像
img = cv2.imread('../data/lena.jpg')
# print(img)
# print(type(img))
# print(img.shape) #300高，300宽,3个通道

#当显示多张图像时，窗口名称不能相同
cv2.imshow('img',img)
cv2.imshow('img1',img)

#保存图像
cv2.imwrite('./data.jpg',img)

#主动进入阻塞等待状态，等待用户按下某一个按键，则停止阻塞
# while True:
#     key = cv2.waitKey()  #ms
#     if key == 27:
#         break
cv2.waitKey()
cv2.destroyAllWindows()

