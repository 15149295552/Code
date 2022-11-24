'''
使用自定义复合类型加载数据
'''
import numpy as np

def loadcsv():
    with open('./aapl.csv','r') as f:
        data = []
        for line in f.readlines():
            data.append(tuple(line[:-1].split(',')))

        res = np.array(data,dtype={'names':['name','open','high','low','close'],
                                   'formats':['U4','f8','f8','f8','f8']})
        return res

data = loadcsv()

print(data)
