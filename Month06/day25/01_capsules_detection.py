# 01_capsules_detection.py
# 利用图像实现胶囊瑕疵检测
import cv2
import numpy as np
import os


# 判断是否为大小头
def balance_detection(img_path, fn, im, im_gray):
    # 模糊
    im_blur = cv2.GaussianBlur(im_gray, (5, 5), 0)
    # 膨胀
    k = np.ones((5, 5), np.uint8)  # 计算核
    im_dilate = cv2.dilate(im_blur, k)  # 膨胀
    cv2.imshow("im_dilate", im_dilate)
    # Canny边沿提取
    im_canny = cv2.Canny(im_dilate, 60, 200)
    cv2.imshow("im_canny", im_canny)
    # 轮廓查找
    # cnts, hie = cv2.findContours(im_canny,  # Opencv4.x
    img, cnts, hie = cv2.findContours(im_canny,  # Opencv3.x
                                      cv2.RETR_LIST,
                                      cv2.CHAIN_APPROX_NONE)
    # 根据周长过滤
    new_cnts = []  # 过滤后的轮廓
    for i in range(len(cnts)):
        cir_len = cv2.arcLength(cnts[i], True)  # 计算轮廓周长
        if cir_len >= 1000:  # 周长超过1000
            new_cnts.append(cnts[i])
    # 根据面积对轮廓排序
    new_cnts = sorted(new_cnts,  # 待排序对象
                      key=cv2.contourArea,  # 排序依据：根据该函数计算结果进行排序
                      reverse=True)  # 倒序排列
    new_cnts = new_cnts[1:2]  # 切出第二个轮廓(切片操作不会降低维度)
    # 绘制轮廓
    im_cnt = cv2.drawContours(im,  # 在三通道图像上绘制
                              new_cnts,  # 绘制过滤后的轮廓
                              -1,  # 绘制所有轮廓
                              (0, 0, 255), 2)  # 颜色、粗细
    cv2.imshow("im_cnt", im_cnt)

    # print(new_cnts)
    # 计算药丸轮廓的边界
    max_x, max_y = new_cnts[0][0][0][0], new_cnts[0][0][0][1]  # 将轮廓第一个点的x/y作为初始值
    min_x, min_y = max_x, max_y

    for cnt in new_cnts[0]:  # cnt是二维数组，里面存放了一个一维数组
        if cnt[0][0] >= max_x:  # 当前点x坐标max_x还大
            max_x = cnt[0][0]
        if cnt[0][0] <= min_x:  # 当前点x坐标min_x还小
            min_x = cnt[0][0]

        if cnt[0][1] >= max_y:  # 当前点y坐标max_y
            max_y = cnt[0][1]
        if cnt[0][1] <= min_y:
            min_y = cnt[0][1]

    red = (0, 0, 255)  # 红色
    # cv2.line(im, (min_x, min_y), (max_x, min_y), red, 2)
    # cv2.line(im, (max_x, min_y), (max_x, max_y), red, 2)
    # cv2.line(im, (max_x, max_y), (min_x, max_y), red, 2)
    # cv2.line(im, (min_x, max_y), (min_x, min_y), red, 2)

    center_y = int((min_y + max_y) / 2)  # 水平中线
    center_up = int((min_y + center_y) / 2)  # 上半部分中线
    center_down = int((max_y + center_y) / 2)  # 下半部分中线

    # cv2.line(im, (min_x, center_y), (max_x, center_y), red, 2) # 绘制中线
    cv2.line(im, (min_x, center_up), (max_x, center_up), red, 2)  # 绘制上中线
    cv2.line(im, (min_x, center_down), (max_x, center_down), red, 2)  # 绘制下中线

    cv2.imshow("im_line", im)

    # 判断药丸轮廓与上、下中线交点
    cross_up = set()  # 存放与上中线的交点
    cross_down = set()  # 存放与下中线的交点

    for cnt in new_cnts[0]:  # 取出每个点
        x, y = cnt[0][0], cnt[0][1]  # 取出点的x/y坐标
        if y == center_up:  # 当前点的y坐标等于上中线y坐标
            cross_up.add((x, y))
        if y == center_down:  # 当前点的y坐标等于下中线y坐标
            cross_down.add((x, y))

    cross_up = list(cross_up)
    cross_down = list(cross_down)

    # 在交点处绘制小圆圈
    for p in cross_up:
        cv2.circle(im, p, 8, red, 2)
    for p in cross_down:
        cv2.circle(im, p, 8, red, 2)
    cv2.imshow("im_circle", im)

    # 计算上、下中线长度
    len_up = abs(cross_up[0][0] - cross_up[1][0])
    len_down = abs(cross_down[0][0] - cross_down[1][0])
    print("len_up:", len_up, " len_down:", len_down)

    if abs(len_up - len_down) >= 10:  # 两条线长度差超过10
        print("大小头:", fn)
        new_path = "capsules/imbal/" + fn  # 新路径
        os.rename(img_path, new_path)  # 移动文件
        print("移动文件成功:%s ===> %s" % (img_path, new_path))
        return True
    else:
        return False


# 判断是否有气泡
def bub_detection(img_path, fn, im, im_gray):
    # 模糊
    im_blur = cv2.GaussianBlur(im_gray, (3, 3), 0)
    # Canny边沿提取
    im_canny = cv2.Canny(im_blur, 60, 240)
    cv2.imshow("im_canny", im_canny)
    # 轮廓查找
    # cnts, hie = cv2.findContours(im_canny,  # Opencv4.x
    img, cnts, hie = cv2.findContours(im_canny,  # Opencv3.x
                                      cv2.RETR_CCOMP,
                                      cv2.CHAIN_APPROX_NONE)

    new_cnts = []  # 过滤后的轮廓
    for i in range(len(cnts)):
        area = cv2.contourArea(cnts[i])  # 计算面积
        cir_len = cv2.arcLength(cnts[i], True)  # 计算周长

        if area >= 10000 or cir_len >= 1000 or area < 5:  # 过滤过大、过小的轮廓
            continue

        if hie[0][i][3] != -1:  # 当前轮廓存在父轮廓(内部轮廓，保留)
            new_cnts.append(cnts[i])

    # 绘制轮廓
    im_cnt = cv2.drawContours(im,  # 在三通道图像上绘制
                              new_cnts,  # 绘制过滤后的轮廓
                              -1,  # 绘制所有轮廓
                              (0, 0, 255), 2)  # 颜色、粗细
    cv2.imshow("im_cnt", im_cnt)

    if len(new_cnts) > 0:  # 经过过滤后的轮廓数量大于0
        print("气泡或黑点:", fn)
        new_path = "capsules/bub/" + fn  # 新路径
        os.rename(img_path, new_path)  # 移动文件
        print("移动文件成功:%s ===> %s" % (img_path, new_path))
        return True
    else:
        return False


# 判断是否为空胶囊
def empty_detection(img_path, fn, im, im_gray):
    # 模糊处理，合并细节
    im_blur = cv2.GaussianBlur(im_gray, (3, 3), 0)
    cv2.imshow("im_blur", im_blur)
    # 二值化
    t, im_bin = cv2.threshold(im_blur, 210, 255, cv2.THRESH_BINARY)
    cv2.imshow("im_bin", im_bin)
    # 轮廓查找
    # cnts, hie = cv2.findContours(im_bin,  # Opencv4.x
    img, cnts, hie = cv2.findContours(im_bin,  # Opencv3.x
                                      cv2.RETR_CCOMP,
                                      cv2.CHAIN_APPROX_NONE)
    # 根据周长过滤
    new_cnts = []  # 过滤后的轮廓
    for i in range(len(cnts)):
        cir_len = cv2.arcLength(cnts[i], True)  # 计算轮廓周长
        if cir_len >= 1000:  # 周长超过1000
            new_cnts.append(cnts[i])

    # 绘制轮廓
    im_cnt = cv2.drawContours(im,  # 在三通道图像上绘制
                              new_cnts,  # 绘制过滤后的轮廓
                              -1,  # 绘制所有轮廓
                              (0, 0, 255), 2)  # 颜色、粗细
    cv2.imshow("im_cnt", im_cnt)

    if len(new_cnts) == 1:  # 只有一个轮廓, 空胶囊
        print("空胶囊:", fn)
        new_path = "capsules/empty/" + fn  # 新路径
        os.rename(img_path, new_path)  # 移动文件
        print("移动文件成功:%s ===> %s" % (img_path, new_path))
        return True
    else:
        return False


if __name__ == "__main__":
    img_dir = "./capsules/"  # 图片所在的目录
    img_files = os.listdir(img_dir)  # 列出目录下所有图片

    for fn in img_files:  # 遍历
        img_path = img_dir + fn  # 文件完整路径

        if os.path.isdir(img_path):  # 目录
            continue

        im = cv2.imread(img_path)  # 读取图片内容
        im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)  # 转灰度图像
        cv2.imshow("im", im)
        cv2.imshow("im_gray", im_gray)

        # 空胶囊判断
        is_empty = False
        is_empty = empty_detection(img_path, fn, im, im_gray)

        # 气泡检测
        is_bub = False
        if not is_empty:  # 等价于if is_empty == False
            is_bub = bub_detection(img_path, fn, im, im_gray)

        # 大小头检测
        is_bal = False
        if (not is_empty) and (not is_bub):  # 不是空胶囊、气泡胶囊
            is_bal = balance_detection(img_path, fn, im, im_gray)

        cv2.waitKey()
        cv2.destroyAllWindows()
