# 1、自定义排序算法（冒泡排序），对以下列表中的元素降序排列
#     lists = [6, 3, 1, 9, 2]
#
#     要求：总结出排序的规则，并实现出程序

'''
    实现
        1 for循环 --> x   轮数
             range(len(lists)-1)

        2 for循环 --> y   次数
             range(x+1, len(lists))

            if lists[x] < lists[y]:
                lists[x], lists[y] = lists[y], lists[x]
'''

lists = [6, 3, 1, 9, 2]

for x in range(len(lists)-1):
    for y in range(x+1, len(lists)):
        if lists[x] < lists[y]:
            lists[x], lists[y] = lists[y], lists[x]

print(lists)

