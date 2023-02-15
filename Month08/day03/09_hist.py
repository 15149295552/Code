'''直方图：统计每个区间内元素的数量'''

import numpy as np
import matplotlib.pyplot as plt

data = np.random.normal(175,5,10000)

plt.hist(data,bins=100,color='dodgerblue',
         edgecolor='white')
plt.show()

#
#

# import cv2
# import matplotlib.pyplot as plt
#
# img = cv2.imread('./sunrise.jpg',0)
# cv2.imshow('img',img)
#
# plt.hist(img.ravel(),bins=256,range=[0,256])
#
# plt.show()
# cv2.waitKey()
# cv2.destroyAllWindows()

