'''
图像的仿射变换(平移，旋转)
'''
import cv2
import numpy as np


def translate(img, x, y):
    h,w = img.shape[:2]
    M = np.float32([[1,0,x],
                    [0,1,y]])
    res = cv2.warpAffine(img,
                         M,  # 平移矩阵
                         (w, h))  # 输出的尺寸
    return res

def rotate(img,angle,center=None):
    h,w = img.shape[:2]
    #计算旋转中心
    if center is None:
        center = (w/2,h/2)

    #生成旋转矩阵
    M = cv2.getRotationMatrix2D(center,angle,1.0)
    res = cv2.warpAffine(img,M,(w,h))
    return res

if __name__ == '__main__':
    img = cv2.imread('../data/Linus.png')
    cv2.imshow('img',img)
    #平移:向右平移50px,向下平移30px
    #水平:左负右正，垂直:上负下正
    res = translate(img,50,30)
    cv2.imshow('res',res)
    #旋转: 正数逆时针，负数顺时针
    res1 = rotate(img,45)
    cv2.imshow('res1',res1)


    cv2.waitKey()
    cv2.destroyAllWindows()
