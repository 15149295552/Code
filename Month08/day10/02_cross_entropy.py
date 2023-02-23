'''
计算交叉熵
'''
import math
import numpy as np
#5个类别
y_true =  [0,   1,  0,  0,  0] #1
pred_y1 = [0.1,0.6,0.1,0.1,0.1] #1
pred_y2 = [0.1,0.7,0.1,0.05,0.05]
pred_y3 = [0.1,0.8,0.03,0.03,0.04]

entropy1 = 0.0
entropy2 = 0.0
entropy3 = 0.0
for i in range(len(y_true)):
    entropy1 += y_true[i] * math.log(pred_y1[i])
    entropy2 += y_true[i] * math.log(pred_y2[i])
    entropy3 += y_true[i] * math.log(pred_y3[i])

print('交叉熵1:',-entropy1)
print('交叉熵2:',-entropy2)
print('交叉熵3:',-entropy3)