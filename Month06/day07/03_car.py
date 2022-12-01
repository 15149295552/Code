'''
小汽车等级预测
作业:优先将训练集和测试集进行标签编码
    如果有能力,有时间,可以进行建模
'''
import pandas as pd

data = pd.read_csv('../data_test/car.txt',
                   header=None)
# print(data.head())

#数据预处理:将字符串类型的数据,转为数值类型
#因为每列的离散值不同,为每列构建自己的标签编码器


#整理输入和输出

#划分训练集测试集(这组数据,不去划分,使用全部数据进行训练)

#构建模型(随机森林)

#训练

test_data = [['high','med','5more','4','big','low','unacc'],
             ['high','high','4','4','med','med','acc'],
             ['low','low','2','4','small','high','good'],
             ['low','med','3','4','med','high','vgood']]
#预测
#预测数据的格式,要和训练数据一致(训练集做了标签编码,测试集也得做标签编码)
# 训练集和测试集的转换规则要一致

#评估
