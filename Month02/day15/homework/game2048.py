"""
    2048核心算法
"""
list_merge = [2, 0, 2, 0]


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


# zero_to_end()
# print(list_merge)

# 2. 定义函数　merge()
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]
def merge():
    """
        合并数据
          核心思想：零元素后移，判断是否相邻相同。如果是则合并.
    """
    zero_to_end()  # 2 2 0 0
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i] += list_merge[i + 1]  # 4 2 0 0
            del list_merge[i + 1]  # 4 0 0
            list_merge.append(0)  # 4 0 0 0


# print(list_merge)

# 3. 向左移动
map = [
    [2, 0, 0, 2],
    [4, 2, 0, 2],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]

def move_left():
    """
        向左移动map
        思想：获取每行，交给list_merge，在通知merge()进行合并
    :return:
    """
    global list_merge
    for item in map:
        list_merge = item
        # merge函数内部操作的数据就是map行数据
        merge()

def move_right():
    """
        向左移动map
        思想：获取每行，交给list_merge，在通知merge()进行合并
    :return:
    """
    global list_merge
    for line in map:
        list_merge = line[::-1]
        merge()
        line[::-1] = list_merge  # 正向取出 反向存入


move_right()
print(map)

# 作业1
# --向上移动：矩阵转置、调用向左移动、矩阵转置
# --向下移动：矩阵转置、调用向右移动、矩阵转置
