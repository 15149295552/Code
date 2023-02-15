'''
read_json
'''
import pandas as pd

data = pd.read_json('../data_test/ratings.json')
# print(data)


df = pd.DataFrame({'Name':['Tom','Jerry','Jack','Rose'],
                   'Age':[18,18,20,20]})
print(df)
print(df.to_json(orient='records'))
print(df.to_json(orient='index'))
print(df.to_json(orient='columns'))
print(df.to_json(orient='values'))

#Excel
# pip3 install xlrd==1.2.0

data = pd.read_excel('../data_test/电信用户流失数据/CustomerSurvival.xlsx')

print(data)

