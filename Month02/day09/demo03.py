"""
    使用容器调用*args函数
"""

def multiplicative(*args):
    value = 1
    for item in args:
        value *= item
    return value

# list_data = [3,43,4,5,6]
# "1_2_3"-->["1","2","3"]-->[1,2,3]
list_data = [int(item) for item in input().split("_")]
print(multiplicative(*list_data))
