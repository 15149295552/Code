'''
json文件的读取以及写入
'''
import pandas as pd

data = pd.read_json('../data_test/ratings.json')

# print(data)


#输出json串,写入到json文件
data = {'Name':['Tom','Jerry','Jack','Rose'],
        'Age':[18,18,20,20]}
df = pd.DataFrame(data,
                  index=['s1','s2','s3','s4'])
print(df)

print(df.to_json(orient='records'))
print(df.to_json(orient='index'))
print(df.to_json(orient='columns'))
print(df.to_json(orient='values'))


