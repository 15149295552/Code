"""
    索引Index
        定位单个元素
        容器名[整数]
"""
message = "我是花果山水帘洞美猴王孙悟空"
#正向索引:  0 1 2 ...           总数-1
#反向索引: -总数          ...  -3-2-1
print(message)
print(message[0])
print(message[2])
print(message[4])
print(message[-1])
print(message[-3])
# IndexError: string index out of range
# print(message[99])
# print(message[-99])
# 字符串长度
# len(容器名)
print(len(message))