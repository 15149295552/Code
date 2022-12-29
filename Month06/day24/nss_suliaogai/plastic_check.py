import os
import numpy as np
import cv2 as cv


# 加载图片路径
im_path = os.listdir('plastic_cap')

im_files_path = [os.path.join('plastic_cap', path) for path in im_path]
# im = cv.imread(im_files_path[6])


for file_path in im_files_path:
    im = cv.imread(file_path)
    # 灰度
    im_gray = cv.cvtColor(im, cv.COLOR_BGR2GRAY)
    # cv.imshow('im_gray', im_gray)

    # 模糊 去噪点
    blurred = cv.GaussianBlur(im_gray, (7, 7), 3)
    # cv.imshow('blurred', blurred)

    # canny边缘检测
    canny = cv.Canny(blurred, 50, 180)
    cv.imshow('canny', canny)
    # 膨胀  边缘连续，进而提取闭合轮廓
    kernel = np.ones((3, 3), np.uint8)
    dilate = cv.dilate(canny, kernel)

    # cv.imshow('dilate', dilate)

    print(file_path)
    cnts, h = cv.findContours(dilate, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    cnts = sorted(cnts, key=cv.contourArea)

    # 取内部轮廓，切片去除最外2层轮廓（圆形）
    new_cnts = cnts[:-2]

    # 取内部轮廓的最外层（6瓣形）
    c = new_cnts[-1]
    length_c = cv.arcLength(c, False)
    area_c = cv.contourArea(c)
    # print('area_c:', area_c) # 好品的轮廓面积在18600~18700之间
    # print('length_c:', length_c)  # 好品的轮廓长度在600~650之间
    # cv.drawContours(im, c, -1, (0, 0, 255), 2)
    # cv.imshow('im', im)

    # 求每个花瓣的面积
    # 确定圆心。先筛选出轮廓外接矩形内部的所有点
    pt = [0, 0]  # 初始个圆心坐标
    r = 0  # 初始个半径
    all_x = [p[0][0] for p in c]  # 轮廓内全部x
    all_y = [p[0][1] for p in c]  # 轮廓内全部y
    min_x = min(all_x)
    min_y = min(all_y)
    max_x = max(all_x)
    max_y = max(all_y)
    # 绘制轮廓外接矩形
    # cv.rectangle(im, (min_x, min_y), (max_x, max_y), (0, 255, 0), 2)
    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            dist = cv.pointPolygonTest(c, (x, y), True)
            if r < dist:
                r = dist
                pt[0], pt[1] = x, y
    # 绘制最大内接圆
    # cv.circle(im, (pt[0], pt[1]), int(r), (255, 0, 0), 2)
    # 最大内接圆面积
    incircle_area = np.pi*r**2
    # print(incircle_area)

    # 在新图上绘制轮廓和外接圆
    new_im = canny.copy()
    # 转成黑色背景
    ret, new_im = cv.threshold(new_im, 255, 0, cv.THRESH_BINARY)
    cv.drawContours(new_im, c, -1, 255, 1)
    cv.circle(new_im, (pt[0], pt[1]), int(r), 255, 1)
    # cv.imshow('new_im', new_im)
    # 膨胀  边缘连续，进而提取闭合轮廓
    kernel = np.ones((3, 3), np.uint8)
    dilate = cv.dilate(new_im, kernel)
    cv.imshow('dilate', dilate)
    # 提取轮廓

    cnts, h = cv.findContours(dilate, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    print(len(cnts))
    cv.drawContours(im, cnts, -1, (0, 0, 255), 1)
    # 根据面积过滤掉内接圆、最外层轮廓，筛选出花瓣轮廓,花瓣面积在700~1200属于正常范围
    count = 0
    for c in cnts:
        area = cv.contourArea(c)
        # print(area)
        if 700 < area < 1200:
            count += 1
            print('花瓣面积:', area)
    # 判断花瓣数量，6个花瓣，且面积均在700~1200范围内，为好品，反之为缺陷
    if count == 6:
        print('花瓣数量：', count, '好品')
    else:
        print('花瓣数量：', count, '缺陷')

    # 根据面积判断，差几个花瓣
    cv.imshow('im', im)
    cv.waitKey()
    cv.destroyAllWindows()
