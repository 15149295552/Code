# 练习2：创建自定义range类，实现下列效果.

# 生成器函数实现
def myRange(stop):
    start = 0
    while start < stop:
        yield start
        start += 1

for number in myRange(5):
    print(number)  # 0 1 2 3 4