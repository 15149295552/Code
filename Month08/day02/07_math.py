import numpy as np
import pandas as pd

ratings = pd.read_json('../data_test/ratings.json')
print(ratings)
fracture = ratings.loc['Fracture']
print(fracture)

#平均值
print(np.mean(fracture))
print(fracture.mean())
print(np.mean(ratings,axis=1))
print(ratings.mean(axis=1))

ary = np.arange(1,9).reshape(2,4)
print(np.mean(ary,axis=0))

#加权均值
print('='* 30)
print(fracture)
weights = [1,10,1,1,1,10,1]
print(np.average(fracture,weights=weights))

#最值以及最值索引
print('最喜欢看这部电影的人是:{},打了{}分'.format(np.argmax(fracture),np.max(fracture)))

print('最喜欢看这部电影的人是:{},打了{}分'.format(fracture.idxmax(),fracture.max()))

print('中位数:',np.median(fracture))