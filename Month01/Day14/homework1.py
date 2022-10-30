# 模拟 zip 的使用生成器函数编写 myzip

# zip(iterable1, iterable2)

def myzip(*iterable):
    # 1 计算可迭代对象的长度最短
    # print(iterable)
    # 假设法
    min_len = len(iterable[0])
    for i in range(1, len(iterable)):
        if min_len > len(iterable[i]):
            min_len = len(iterable[i])

    # 2 将多个可迭代对象对应位置上的元素组合成元组
    # for i in range(min_len):
    #     yield tuple((iterable[l][i] for l in range(len(iterable))))

    # 方法2:
    for i in range(min_len):
        list_data = []
        for l in range(len(iterable)):
            list_data.append(iterable[l][i])
        yield tuple(list_data)

t1 = [11, 22, 33, 44]
t2 = ('a', 'b', 'c', 'd', 'f')
t3 = ('A', 'B', 'C')
for data in myzip(t1, t2, t3):
    print(data)