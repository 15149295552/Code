"""
编写一个函数，打印所有的水仙花数
水仙花数：是一个三位数，个位立方 + 十位数的立方+百位数的立方=自身
"""
def print_num():
    for i in range(100,1000):
        bai = i // 100
        shi = i // 10 % 10 
        ge = i % 10 
        if bai ** 3 + shi ** 3 + ge ** 3 == i:
            print(i)

print_num()
