"""
    迭代iteration：每一次对过程的重复称为一次“迭代”，
         而每一次得到的结果作为下一次开始。
    迭代器iterator:完成迭代过程的对象
    可迭代对象iterable:创建迭代器对象
"""

message = "我是花果山水帘洞美猴王齐天大圣"
# 迭代
# for item in message:
#     print(item)

# 原理
# 1. 获取迭代器对象
iterator = message.__iter__()
while True:
    try:
        # 2. 获取下一个元素
        item = iterator.__next__()
        print(item)
        # 3. 如果停止迭代则结束循环
    except StopIteration:
        break
