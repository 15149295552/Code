"""
    给定一串字典或列表,找出指定的(前n个)最大值?最小值?
"""

"""
def get_most_value(sequence):
    max_value = sequence[0]
    min_value = sequence[0]
    for i in range(1,len(sequence)):
        if max_value < sequence[i]:
            max_value = sequence[i]
        if min_value > sequence[i]:
            min_value = sequence[i]
    return max_value,min_value

list01 = [1, 9, 8, 6, 0, 8, 6, 3, 3, 4]
print(get_most_value(list01))
"""

"""
def get_most_value(sequence):
    max_value = sequence[0]
    min_value = sequence[0]
    for i in range(1,len(sequence)):
        if max_value[0] < sequence[i][0]:
            max_value = sequence[i]
        if min_value[0] > sequence[i][0]:
            min_value = sequence[i]
    return max_value,min_value

list02 = [[1, 9], [8, 6], [0, 8], [6, 3], [3, 4]]
print(get_most_value(list02))
"""

"""
def get_most_value(sequence):
    max_value = sequence[0]
    min_value = sequence[0]
    for i in range(1, len(sequence)):
        if max_value["n"] < sequence[i]["n"]:
            max_value = sequence[i]
        if min_value["n"] > sequence[i]["n"]:
            min_value = sequence[i]
    return max_value, min_value

list03 = [{"n": 9}, {"n": 6}, {"n": 8}, {"n": 3}, {"n": 4}]
print(get_most_value(list03))
"""

def get_most_value(sequence,n,condition):
    max_value = sequence[0]
    min_value = sequence[0]
    for i in range(1,n):
        # if max_value[0] < sequence[i][0]:
        # if max_value["n"] < sequence[i]["n"]:
        if condition(max_value) < condition(sequence[i]):
            max_value = sequence[i]
        if condition(min_value) > condition(sequence[i]):
            min_value = sequence[i]
    return max_value,min_value

list02 = [[1, 9], [8, 6], [2, 8], [0, 3], [3, 4]]
list03 = [{"n": 9}, {"n": 6}, {"n": 8}, {"n": 0}, {"n": 4}]
print(get_most_value(list02,3, lambda item: item[0]))
print(get_most_value(list03,3, lambda item: item["n"]))
