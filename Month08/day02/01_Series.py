'''
Series创建、访问示例
'''
import numpy as np
import pandas as pd

s = pd.Series([100,90,80,70],
              index=['zs','ls','ww','sl'])
# print(s[0])
# print(s[-1]) pandas不支持反向索引
# print(s)
# print(s['zs'])
# print(s[-1])

s = pd.Series({'zs':100,'ls':90,'ww':80})
# print(s)

#生成一维数据，10个0.2
# print(np.zeros(10) + 0.2)
# print(np.ones(10) / 5)
# s = pd.Series(0.2,index=range(10))
# print(s)


#访问Series中数据:索引、切片、掩码
s = pd.Series([100,90,80,70],
              index=['zs','ls','ww','sl'])
#位置索引、标签索引
# print(s[0])
# print(s[:2])
# print(s[[0,2,3]])
# print(s['ww'])
# print(s['zs':'ls'])# 标签索引切片包含终止位置
# print(s[['zs','ls','sl']])

# print(s.values)
# print(s.index)

#简单测试时间日期类型
data = ['2023','2023-02','2023-03-01','2023/04/01',
        '2023-5-1 01:01:01','01 Jun 2023',
        '20230701','2023/8/1','01-02-1932']
s = pd.Series(data)

res = s.astype('M8')
print(res)


