"""

"""
# 不用for循环获取列表所有元素
list01 = [34, 54, 54, 56, 7]
iterator = list01.__iter__()
while True:
    try:
        item = iterator.__next__()
        print(item)
    except StopIteration:
        break

# 面试题:不使用for循环,获取字典所有键值对.
dict01 = {"a": 34, "b": 54, "c": 54}
iterator = dict01.__iter__()
while True:
    try:
        key = iterator.__next__()
        print(key, dict01[key])
    except StopIteration:
        break
