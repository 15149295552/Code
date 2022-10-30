"""
    2048核心算法
"""
list_merge = [2, 0, 0, 2]


# 删除第一个0元素
# for i in range(len(list_merge)):
#     if list_merge[i] == 0:
#         del list_merge[i]
#         break #只要删除了元素,任务即可完成

# 删除所有0元素
# for i in range(len(list_merge)-1,-1,-1):
#     if list_merge[i] == 0:
#         del list_merge[i]

# 2处错误:
# -- 切片因为从最后元素开始到最后元素结束，所以没有取得元素
# -- 删除变量item与列表无关
# for item in list_merge[len(list_merge)-1:-1:-1]:
#     if item == 0:
#         del item


# 正序删除
# del list_merge[1] # 会导致后面元素向前移动
# del list_merge[2] # 删除的是2，并非是0

# 倒序删除
# del list_merge[2] # 对左侧0元素没有影响
# del list_merge[1] #

# 1. 定义函数　zero_to_end()
# [2,0,2,0]  -->  [2,2,0,0]
# [2,0,0,2]  -->  [2,2,0,0]
# [2,4,0,2]  -->  [2,4,2,0]
def zero_to_end():
    """
        零元素向后移动
        思想：从后向前判断，如果是0则删除,在末尾追加.
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# 2. 定义函数　merge()
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]
def merge():
    """
        合并数据
          思想：零元素后移，判断是否相邻相同。
               如果是则合并(后一个元素累加到前一个之上,再删除后一个元素).
    """
    zero_to_end()
    # 因为判断i删除i+1,所以不用倒序删除
    for i in range(len(list_merge) - 1):  # 0  1  2
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


merge()
print(list_merge)  # 4  0  0  0
