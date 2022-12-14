'''
图像的仿射变换：平移和旋转
'''
import cv2
import numpy as np

#平移
def translate(img, x, y):
    #输出的尺寸和原始图像一致
    h,w = img.shape[:2]  # (高,宽,通道数)
    #平移矩阵
    M = np.float32([[1,0,x],
                    [0,1,y]])
    res = cv2.warpAffine(img,  # 变换的图像
                         M,  # 平移矩阵
                         (w, h))  # 输出图像的尺寸
    return res


#旋转
def rotate(img,angle,center=None):
    '''
    :param img: 图像
    :param angle: 旋转角度
    :param center: 旋转中心
    :return:
    '''
    h,w = img.shape[:2]
    #如果没有传入center，默认使用图像的正中心
    if center is None:
        center = (w/2,h/2)

    #旋转矩阵
    M = cv2.getRotationMatrix2D(center,angle,1.0)#旋转中心，旋转角度，缩放比例

    res = cv2.warpAffine(img,
                         M,#旋转矩阵
                         (w,h))#输出图像的宽度和高度
    return res

if __name__ == '__main__':
    img = cv2.imread('../data/Linus.png')
    cv2.imshow('img',img)
    #平移
    #水平方向x   正数：向右移动  负数：向左移动
    #垂直方向y   正数：向下移动  负数：向上移动
    res1 = translate(img,0,50)
    cv2.imshow('res1',res1)

    #旋转
    #旋转角度，正数：逆时针  负数：顺时针
    res2 = rotate(img,-45)
    cv2.imshow('res2',res2)

    cv2.waitKey()
    cv2.destroyAllWindows()

