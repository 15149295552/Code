'''
图像的裁剪:随机裁剪，中心裁剪
'''
import cv2
import numpy as np

#随机裁剪
def random_crop(img,c_w,c_h):
    h,w = img.shape[:2]
    start_x = np.random.randint(0,w-c_w) #起始的x坐标
    start_y = np.random.randint(0,h-c_h) #起始的y坐标

    new_img = img[start_y:start_y+c_h,start_x:start_x+c_w]
    return new_img

def center_crop(img,c_w,c_h):
    h,w = img.shape[:2]

    start_x = int(w / 2) - int(c_w / 2)
    start_y = int(h / 2) - int(c_h / 2)

    new_img = img[start_y:start_y + c_h, start_x:start_x + c_w]
    return new_img

if __name__ == '__main__':
    img = cv2.imread('../data/banana_1.png')
    cv2.imshow('img',img)

    #随机裁剪
    random = random_crop(img,200,200)
    cv2.imshow('random',random)
    #中心裁剪
    center = center_crop(img,200,200)
    cv2.imshow('center',center)

    cv2.waitKey()
    cv2.destroyAllWindows()