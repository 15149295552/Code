'''
读取文本文件
'''
import pandas as pd

data = pd.read_csv('../data_test/aapl.csv',
                   header=None,
                   names=['name','date','_','open',
                          'high','low','close','__'],
                   index_col='date',
                   usecols=['name','date','open',
                            'high','low','close'])

print(data)

data.to_csv('./new_aapl.csv')







