"""
    两层for循环嵌套
"""
"""
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print() # 换行
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print() # 换行
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print("*",end = " ")
print() # 换行
"""

"""
for c in range(5):
    print("*",end = " ")
print() # 换行
for c in range(5):
    print("*",end = " ")
print() # 换行
for c in range(5):
    print("*",end = " ")
print() # 换行
"""

for r in range(3):  # 0     1      2
    for c in range(5):  # 0~5   0~5    0~5
        print("*", end=" ")
    print()  # 换行
