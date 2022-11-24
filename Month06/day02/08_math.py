'''
numpy,pandas中提供的数学指标
'''
import numpy as np
import pandas as pd

ratings = pd.read_json('../data_test/ratings.json')
print(ratings)

fracture = ratings.loc['Fracture']
# print(fracture)

#平均值
print(np.mean(fracture))
#对dataframe求平均值,如果不写axis,axis默认为0,求每列的平均值
print(np.mean(ratings,axis=0))
print(np.mean(ratings,axis=1))
#对二维数组求平均值,如果不设定axis,则将所有数据求平均值
#axis=1,每行的平均值,axis=0每列的平均值
print(np.mean(ratings.values))


print(fracture.mean())
print(ratings.mean()) #axis=0
print(ratings.mean(axis=1))


#加权均值
print('=' * 40)

print(np.average(fracture,weights=[1,10,1,1,1,10,1]))


#最值,最值的索引
#np中的最值索引返回的是位置索引
print('=' * 30)
print('最高分为:{},谁打的:{}'.format(np.max(fracture),
                                   np.argmax(fracture)))
# pandas中的最值索引,返回的是标签索引
print('最高分为:{},谁打的:{}'.format(fracture.max(),
                                   fracture.idxmax()))