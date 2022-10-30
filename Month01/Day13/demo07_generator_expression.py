# 生成器表达式

# 通过生成器生成 1-10之间整数的平方
def genderate_int(stop):
    for i in range(1, stop):
        yield i ** 2

print(list(genderate_int(6)))


exp = (i ** 2 for i in range(1, 10))
print(exp)
for item in exp:
    print(item)

# 通过生成器生成 1-10之间偶数的平方
exp = (i ** 2 for i in range(1, 10) if i % 2 == 0)
for item in exp:
    print(item)