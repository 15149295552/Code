import cv2 as cv
import numpy as np
import os


def ng_check(img_path, img_file, image, im_gray):
    f_1 = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
    im_f1 = cv.filter2D(im_gray, -1, f_1)  # 卷一下

    cv.imshow('00', im_f1)
    imgcanny = cv.Canny(im_f1, 80, 200)  # 边沿提取
    # cv.imshow('00canny', imgcanny)
    imgcanny2 = cv.Canny(im_gray, 80, 200)  # 原图ｃａｎｎｙ
    # cv.imshow('01canny', imgcanny2)

    kernel = np.ones((3, 3), np.uint8)
    dilation = cv.dilate(imgcanny2, kernel, iterations=5)  # 将ｃａｎｎｙ２膨胀
    # cv.imshow('di', dilation)

    dst = cv.subtract(imgcanny, dilation)  # canny1 - 膨胀后canny2
    # cv.imshow('03', dst)

    dst2 = cv.dilate(dst, kernel, iterations=3)  # 差运算后膨胀
    # cv.imshow('dst2', dst2)

    image, contours, hierarchy = cv.findContours(dst2, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)  # 轮廓

    new_cnts = []

    for cnt in contours:  # 遍历每个轮廓
        # arcLength函数计算周长
        circle_len = cv.arcLength(cnt,
                                  True)  # 是否为封闭轮廓
        if circle_len >= 600 and circle_len <= 720:
            new_cnts.append(cnt)
            # im_cnt = cv.drawContours(image, new_cnts, -1, (0, 0, 255), 3)
            # cv.imshow("im_cnt", im_cnt)

    draw_g(new_cnts)


def draw_g(new_cnts):
    max_x, max_y = new_cnts[0][0][0][0], new_cnts[0][0][0][1]
    min_x, min_y = max_x, max_y

    # 遍历轮廓坐标，找出最大最大x,y, 最小x,y
    for item in new_cnts:
        for cnt in item:
            if cnt[0][0] >= max_x:  # 如果当前点的x坐标大于max_x
                max_x = cnt[0][0]
            if cnt[0][0] <= min_x:  # 如果当前点的x坐标小于min_x
                min_x = cnt[0][0]
            if cnt[0][1] >= max_y:
                max_y = cnt[0][1]
            if cnt[0][1] <= min_y:
                min_y = cnt[0][1]
    # im_cnt2 = cv.drawContours(image, new_cnts, -1, (0, 0, 255), 3)
    # cv.imshow("im_cnt2", im_cnt2)

    # ----------------------------------红色部分
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)  # hsv
    hsv1 = hsv[0:image.shape[0], 0:max_x]  # 裁剪

    minRed = np.array([0, 135, 135])
    maxRed = np.array([50, 255, 255])  # red

    mask = cv.inRange(hsv1, minRed, maxRed)
    red = cv.bitwise_and(hsv1, hsv1, mask=mask)  # mask

    im_mean_blur = cv.blur(red, (3, 3))  # blur

    k = np.ones((7, 7), np.uint8)
    r1 = cv.morphologyEx(im_mean_blur, cv.MORPH_CLOSE, k, iterations=2)  # 闭运算
    # cv.imshow("r1", r1)

    img_gray_r1 = cv.cvtColor(r1, cv.COLOR_BGR2GRAY)
    red_img, red_contours, red_hierarchy = cv.findContours(img_gray_r1, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

    # red_im_cnt = cv.drawContours(image, red_contours, -1, (0, 0, 255), 3)
    # cv.imshow("red_im_cnt", red_im_cnt)

    new_cnts2 = []

    for cnt2 in red_contours:  # 遍历每个轮廓
        # arcLength函数计算周长
        circle_len = cv.arcLength(cnt2,
                                  True)  # 是否为封闭轮廓
        print('redlen', circle_len)

        if circle_len > 1100:
            new_cnts2.append(cnt2)
    if new_cnts2 == []:
        print('无瑕疵')
        font = cv.FONT_HERSHEY_SIMPLEX
        imgzi = cv.putText(image, 'none', (50, 300), font, 1.2, (255, 255, 255), 2)
        cv.imshow("imgzi", imgzi)
        return

    red_max_x, red_min_x = new_cnts2[0][0][0][0], new_cnts2[0][0][0][0]
    for item2 in new_cnts2:
        for cnt2 in item2:
            if cnt2[0][0] >= red_max_x and cnt2[0][0] >= max_x:
                red_max_x = max_x
            elif cnt2[0][0] >= red_max_x:  # 如果当前点的x坐标大于max_x
                red_max_x = cnt2[0][0]
            if cnt2[0][0] <= red_min_x:  # 如果当前点的x坐标小于min_x
                red_min_x = cnt2[0][0]

    # ------------------画图

    cv.line(image, (red_min_x, min_y), (red_max_x, min_y), (0, 0, 255), 3)
    cv.line(image, (red_min_x, min_y), (red_min_x, max_y), (0, 0, 255), 3)
    cv.line(image, (red_min_x, max_y), (red_max_x, max_y), (0, 0, 255), 3)
    cv.line(image, (red_max_x, min_y), (red_max_x, max_y), (0, 0, 255), 3)

    cv.line(image, (min_x, min_y), (max_x, min_y), (0, 255, 0), 1)
    cv.line(image, (min_x, min_y), (min_x, max_y), (0, 255, 0), 1)
    cv.line(image, (min_x, max_y), (max_x, max_y), (0, 255, 0), 1)
    cv.line(image, (max_x, min_y), (max_x, max_y), (0, 255, 0), 1)
    print(" min_x:", min_x, " min_y:", min_y,
          " max_x:", max_x, " max_y:", max_y)
    # cv.imshow("im_line", image)
    stain_area = (red_max_x - red_min_x) * (max_y - min_y)
    font = cv.FONT_HERSHEY_SIMPLEX
    imgz2 = cv.putText(image, 'Stain Area:%d' % (stain_area), (50, 300), font, 1.2, (255, 255, 255), 2)
    cv.imshow("imgz2", imgz2)


if __name__ == "__main__":
    # 加载所有待检测图像
    img_dir = "ng"
    # img_dir = "ok"
    img_files = os.listdir(img_dir)  # 列出所有待检测图像

    for img_file in img_files:
        # 拼接完整图片路径
        img_path = os.path.join(img_dir, img_file)
        if os.path.isdir(img_path):  # 子目录直接跳过
            continue
        image = cv.imread(img_path, 1)
        im_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)  # 转灰度图像
        ng_check(img_path, img_file, image, im_gray)

        cv.waitKey()
        cv.destroyAllWindows()
