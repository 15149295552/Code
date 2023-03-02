'''皮尔逊相关系数'''

import pandas as pd
import numpy as np

data = pd.read_json('../data_test/ratings.json')
print(data)

# corr = np.corrcoef(data['John Carson'],data['Michael Henry'])
# print(corr)
corr = data.corr()

print(corr[corr>0.6])