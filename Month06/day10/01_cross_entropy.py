'''
计算多个类别的交叉熵
'''
import math
import numpy as np

          #苹果,香蕉,橙子,葡萄,梨
y_ture =  [0,   1,  0,  0,  0]
pred_y1 = [0.1,0.6,0.1,0.1,0.1] #每个类别的概率不能为0
pred_y2 = [0.1,0.7,0.1,0.05,0.05]
pred_y3 = [0.1,0.8,0.04,0.03,0.03]

cross_entropy1 = 0.0
cross_entropy2 = 0.0
cross_entropy3 = 0.0
for i in range(len(y_ture)):
    cross_entropy1 += y_ture[i] * math.log(pred_y1[i])
    cross_entropy2 += y_ture[i] * math.log(pred_y2[i])
    cross_entropy3 += y_ture[i] * math.log(pred_y3[i])
avg_cost1 = -cross_entropy1 / len(pred_y1)
avg_cost2 = -cross_entropy2 / len(pred_y2)
avg_cost3 = -cross_entropy3 / len(pred_y3)

print('cross_entropy1:',avg_cost1)
print('cross_entropy2:',avg_cost2)
print('cross_entropy3:',avg_cost3)





# BGR
# [[[255,0,0],    [0,0,255],[0,255,0],[255,0,0]],
#  [[255,255,255],[0,0,0],  [0,255,0],[0,255,0]],
#  [[0,0,0],      [0,0,255],[0,0,255],[0,255,0]],
#  [[0,0,0],      [0,0,255],[0,0,255],[0,0,255]]]
#
# [[0,255,255,255],
#  [255,0,255,255],
#  [255,255,0,255],
#  [255,255,255,0]]



