'''
关联规则：Apriori
'''

def loadData():
    with open('./item.txt','r') as f:
        data = f.readlines()
        res = []
        for i in data:
            res.append(i.strip().split(','))
        return res

#遍历样本数据集，建立1项集的候选集
def createC1(dataSet):
    #记录每项物品的列表
    C1 = []
    for transation in dataSet:
        for item in transation:
            if [item] not in C1:
                C1.append([item])
    C1.sort()
    return list(map(frozenset,C1))
    #[{物品},{物品},{物品}]


def scanD(D, Ck, min_support):
    ssCnt = {}
    #遍历候选集中每项物品，在样本中出现的次数
    for tid in D:
        for can in Ck:
            #判断候选集中的项，是否为样本的子集
            if can.issubset(tid):
                if can not in ssCnt:
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    #计算相对支持度  出现次数 / 样本总数
    numItems = float(len(D))
    ret_list = []
    support_data = {}
    #遍历候选集中的每项记录，计算支持度
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= min_support:
            ret_list.insert(0,key)
        support_data[key] = support#满足不满足都保存
    return ret_list,support_data


def aprioriGen(Lk, k):
    ret_list = []
    for i in range(len(Lk)):
        for j in range(i+1,len(Lk)):
            L1 = list(Lk[i])[:k-2]
            L2 = list(Lk[j])[:k-2]
            L1.sort()
            L2.sort()
            if L1 == L2:
                ret_list.append(Lk[i] | Lk[j])
    return ret_list




def Apriori(dataSet, min_support):
    #生成1项集
    C1 = createC1(dataSet)
    #对样本数据，映射成固定集合
    D = list(map(frozenset,dataSet))
    #过滤最小支持度，得到频繁项集
    L1,supportData = scanD(D,C1,min_support)

    # [[{物品},{物品}]]
    L = [L1] #存放所有项集的频繁项集
    k = 2

    while (len(L[k-2])>0):
        #根据当前的频繁项集，生成下一个项集的候选集
        Ck = aprioriGen(L[k-2],k)
        Lk,supk = scanD(D,Ck,min_support)
        L.append(Lk)
        supportData.update(supk)
        k += 1
    return L,supportData



if __name__ == '__main__':
    dataSet = loadData()
    L,sup = Apriori(dataSet,min_support=0.5)

    # for i in L:
    #     print(i)
    # print(sup)

休息15分钟， 17：20回来