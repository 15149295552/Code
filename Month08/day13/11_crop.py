'''
图像的裁剪:随机裁剪、中心裁剪
本质：利用数组的切片
'''
import numpy as np
import cv2

def random_crop(img,cw,ch):
    #随机的起始坐标x,y
    start_x = np.random.randint(0,img.shape[1]-cw)
    start_y = np.random.randint(0,img.shape[0]-ch)

    new_img = img[start_y:start_y+ch,start_x:start_x+cw]
    return new_img

def center_crop(img,cw,ch):
    #起始坐标x,y
    start_x = int(img.shape[1] / 2) - int(cw / 2)
    start_y = int(img.shape[0] / 2) - int(ch / 2)

    new_img = img[start_y:start_y+ch,start_x:start_x+cw]
    return new_img

if __name__ == '__main__':
    img = cv2.imread('../data/banana_1.png')
    cv2.imshow('img',img)
    #随机裁剪
    res = random_crop(img,200,200)
    cv2.imshow('res',res)
    #中心裁剪
    center = center_crop(img,200,200)
    cv2.imshow('center',center)


    cv2.waitKey()
    cv2.destroyAllWindows()


