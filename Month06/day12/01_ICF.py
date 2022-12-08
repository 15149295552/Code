'''
基于物品的协同过滤 ICF
'''
import pandas as pd
import math

class ItemBasedCF:
    #初始化对象
    def __init__(self,data_file):
        self.data_file = data_file
        self.readData()

    #数据读取
    def readData(self):
        self.data = dict()
        for line in open(self.data_file):
            user,item,score,time = line.strip().split(',')
            #用户-物品评分矩阵{用户:{电影:打分,....,....}}
            self.data.setdefault(user,{})
            #分数赋值
            self.data[user][item] = int(score)

    #物品间的相似度
    def ItemSmilarity(self):
        C = dict() #物品-物品的共现矩阵
        N = dict() #物品被多少个不同的用户购买

        #遍历所有数据,获得用户发生过行为的物品
        for user,items in self.data.items():#{用户:{电影:打分,....,....}}
            #遍历该用户的每个物品
            for i in items.keys():
                #只要看过这部电影,次数+1
                N.setdefault(i,0)
                N[i] += 1
                #物品-物品共现矩阵 + 1
                C.setdefault(i,{}) #{电影1:{电影2:次数,电影3:次数},...}
                #遍历该用户的所有物品
                for j in items.keys():
                    if i == j:
                        continue
                    C[i].setdefault(j,0)
                    C[i][j] += 1
        # print(N) #物品被多少个不同的用户购买
        # print(C)# 物品-物品共现矩阵

        #计算相似度
        self.W = dict()
        #遍历物品-物品的共现矩阵的所有项
        for i,related_items in C.items():#{电影1:{电影2:次数,电影3:次数},...}
            #存放物品间的相似度
            self.W.setdefault(i,{})#{电影1:{电影2:相似度,电影3:相似度},...}
            for j,cij in related_items.items():
                self.W[i][j] = cij / math.sqrt(N[i] * N[j])

        return self.W

    #生成推荐列表
    def Recommend(self,user,k=3,N=10):
        #用户user对物品的偏好值
        rank = dict()
        #用户user产生过的行为物品项，以及评分
        action_item = self.data[user] # {电影1：打分，电影2：打分....}
        #找到user看过的电影item,找到与item相似的电影，从大到小排列
        # 电影1：电影2，电影3，电影4....   只取最大的前三个
        for item,score in action_item.items():
            # {电影1:{电影2:相似度,电影3:相似度},...}
            for j,wj in sorted(self.W[item].items(),
                   key=lambda x:x[1],reverse=True)[0:k]:
                #如果该物品为当前物品,已经看过：
                if j in action_item.keys():
                    continue
                #计算用户user对推荐物品的偏好值
                rank.setdefault(j,0)
                rank[j] += score * wj

               # 按照评分大小，为User推荐前N个物品

        # rank  {电影1：推荐值,电影2:推荐值}
        return sorted(rank.items(),key=lambda x:x[1],reverse=True)[0:N]


if __name__ == '__main__':
    # data = pd.read_csv('../data_test/movielens电影数据/ratings.dat',
    #                    sep='::',
    #                    engine='python',
    #                    header=None)
    # data = data.head(1000)
    # data.to_csv('data.csv',header=None,index=False)

    icf = ItemBasedCF('data.csv')
    icf.ItemSmilarity()
    res = icf.Recommend('3')

    for i in res:
        print(i)







