'''
基于物品的协同过滤ICF
'''
import math

import pandas as pd


class ItemBasedCF:
    # 初始化对象
    def __init__(self, data_file):
        self.data_file = data_file
        self.read_data()

    def read_data(self):
        # 用户-评分表
        # {用户:{电影:评分,电影:评分}}
        self.data = {}
        for line in open(self.data_file):
            user, item, score, time = line.strip().split(',')
            # 用户-评分矩阵
            self.data.setdefault(user, {})
            self.data[user][item] = int(score)
        # print(self.data)

    # 计算相似度
    def ItemSmilarty(self):
        self.C = {}  # 物品-物品的共现矩阵 {电影1:{电影2:次数，电影3:次数}}
        self.N = {}  # 每个物品单独出现的次数   {电影名:次数}

        # 遍历数据，生成用户对不同物品发生的行为
        for user, items in self.data.items():
            for i in items.keys():  # 遍历每个电影名
                self.N.setdefault(i, 0)
                self.N[i] += 1  # 次数+1
                # 共现矩阵
                self.C.setdefault(i, {})
                for j in items.keys():
                    if i == j:  # 如果为当前电影，不记录
                        continue
                    self.C[i].setdefault(j, 0)
                    self.C[i][j] += 1
        # 计算相似度   i∩j / sqrt(i*j)

        # 遍历物品-物品共现矩阵 {电影1:{电影2:次数，电影3:次数}}
        self.W = {}  # {电影1:{电影2:相似度，电影3:相似度}}
        for i, related_items in self.C.items():
            self.W.setdefault(i, {})
            for j, cij in related_items.items():
                self.W[i][j] = cij / math.sqrt(self.N[i] * self.N[j])

        return self.W

    # 生成推荐列表
    def Recommend(self, user, K=3,N=10):
        # 用户对某个商品的偏好值
        rank = {}
        # 拿到user用户发生过行为的商品和评分
        action_item = self.data[user]
        # 遍历行为商品，找到与行为商品的相似物品的前三个
        for item, score in action_item.items():
            for j, wj in sorted(self.W[item].items(),
                                key=lambda x: x[1],
                                reverse=True)[0:K]:
                #如果物品j发生过行为，跳过
                if j in action_item.keys():
                    continue
                #没看过，计算推荐值
                rank.setdefault(j,0)
                rank[j] += wj * score
        #按照推荐值进行排序，取到前10个推荐结果
        res = dict(sorted(rank.items(),key=lambda x:x[1],reverse=True)[0:N])
        return res



if __name__ == '__main__':
    # data = pd.read_csv('../data_test/movielens电影数据/ratings.dat',
    #                    header=None,
    #                    sep='::',
    #                    engine='python')
    # data = data.head(1000)
    # data.to_csv('data.csv',header=None,index=False)

    icf = ItemBasedCF('./data.csv')
    icf.ItemSmilarty()
    print(icf.Recommend('3'))
