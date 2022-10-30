# 模拟 enumerate的使用生成器函数编写 myenumerate

# enumerate(iterable, start=0)

def myenumerate(iterable, start=0):
    value = start
    for item in iterable:
        yield (value, item)
        value += 1

t = (22, 44, 66, 88)
for item in myenumerate(t, 3):
    print(item)