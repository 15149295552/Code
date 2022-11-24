'''
读取文本文件
'''
import pandas as pd

data = pd.read_csv('../data_test/aapl.csv',
                   header=None,
                   names=['name','date','_','open','high','low','close','__'],
                   index_col='date',
                   usecols=['name','open','high','low','close','date'])

print(data)

#写入到csv文件中
data.to_csv('./new_data.csv')


