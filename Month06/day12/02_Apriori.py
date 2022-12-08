'''
关联规则:Apriori
'''

def loadDataSet():
    with open('./item.txt','r') as f:
        data = f.readlines() #[第一行，第二行......]
        res = []
        for i in data:
            res.append(i.strip().split(','))
        return res


def createC1(dataSet):
    #记录每项物品的列表
    C1 = [] #[[bread],[milk],[tea]]
    #遍历每个样本的每个商品
    for i in dataSet:
        for item in i:
            #如果该物品没在C1中
            if [item] not in C1:
                C1.append([item])
    #排序
    C1.sort()
    #将列表内的元素映射到frozenset类型中，返回列表
    #固定集合，一旦被建立，用户不能修改
    # [frozenset{'bread'},frozenset{'tea'},....]
    return list(map(frozenset,C1))


def scanD(D, Ck, min_Support):
    #候选集Ck中的每项物品，在所有物品记录中出现的次数
    ssCnt = {}
    # 遍历样本数据，对比候选集中的每项和样本中的每项，统计次数
    for tid in D:#每一个样本，固定集合
        for can in Ck: #固定集合
            #如果在tid中，can出现了，则can是tid的子集
            if can.issubset(tid):
                #如果候选集Ck中该项第一次被统计到，次数为1
                if can not in ssCnt:
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    #数据集中总的记录数，用于计算支持度
    numItems = float(len(D))

    #记录最小支持度过滤后的频繁项集
    retList = []
    #记录每项的支持度，不管满足不满足最小支持度，都去记录
    supportData = {}
    #遍历ssCnt每项出现的次数，计算支持度
    for key in ssCnt:
        support = ssCnt[key] / numItems #支持度:出现次数 / 总数
        supportData[key] = support #记录支持度，满足不满足都保存
        #过滤最小支持度
        if support >= min_Support:
            retList.insert(0,key)

    return retList,supportData


def aprioriGen(Lk, k):
    '''
    使用Lk ---》 Lk+1 的候选集
    :param Lk: 频繁项集
    :param k: 候选集的元素个数　k=2　两个商品共同出现
    :return:
    '''
    retList = []
    for i in range(len(Lk)):
        for j in range(i+1,len(Lk)):
            L1 = list(Lk[i])[:k - 2]
            L2 = list(Lk[j])[:k - 2]
            #排序
            L1.sort()
            L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])

    return retList


def apriori(dataSet, min_Support):
    #生成1项集
    C1 = createC1(dataSet)
    #把数据集映射为列表套固定集合，可以去除掉重复数据
    D = list(map(frozenset,dataSet))
    #过滤最小支持度，得到频繁1项集，拿到每项的支持度
    L1,supportData = scanD(D,C1,min_Support)

    #L,存放所有的频繁项集
    L = [L1] #[[forzenset{'bread'},...,....],[L2频繁项集]]
    k = 2 #从1项集的频繁项集，生成2项集的候选集

    #根据L1找L2,根据L2找L3.....
    # 如果当前频繁项集中有元素，可以生成下一个项集的候选集
    # 如果当前频繁项集中没有元素，则停止生成
    while len(L[k-2]) > 0:
        #要根据当前频繁项集，生成下一个项集的候选集
        Ck = aprioriGen(L[k-2],k)
        #进行最小支持度的过滤
        Lk,supk = scanD(D,Ck,min_Support)
        #更新支持度字典
        supportData.update(supk)
        #将新生成频繁ｋ项集添加的Ｌ中
        L.append(Lk)
        #k生成完当前项集，＋＝　１
        k += 1

    return L,supportData




if __name__ == '__main__':
    dataSet = loadDataSet()
    L,supdata = apriori(dataSet,min_Support=0.5)

    # for i in L:
    #     print(i)

    # print(supdata)


