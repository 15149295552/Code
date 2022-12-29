from Stitcher import Stitcher
import cv2

# 读取拼接图片
imageA = cv2.imread("left_01.png")
imageB = cv2.imread("right_01.png")


# imageA = cv2.imread('box_left.jpg')
# imageB = cv2.imread('box_right.jpg')
# imageA = cv2.resize(imageA,(0,0),fx=0.4,fy=0.4)
# imageB = cv2.resize(imageB,(0,0),fx=0.4,fy=0.4)

# 把图片拼接成全景图
stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# 显示所有图片
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches", vis)
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()