#
def func01(p1, p2, p3):
    p1[0] = 100
    p2 = 200
    p3[:] = [300]
    return p2

a = [10]
b = [20]
c = [30]
d = func01(a, b[0], c[:])
print(a)  # ?
print(b)  # ?
print(c)  # ?
print(d)
# 练习3：根据下列代码，创建降序排列函数。
