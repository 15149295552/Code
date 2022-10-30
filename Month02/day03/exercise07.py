"""
# 练习2：
# 在终端中显示0 1 2 3
# 在终端中显示2 3 4 5 6
# 在终端中显示1 3 5 7
# 在终端中显示8 7 6 5 4
# 在终端中显示-1 -2 -3 -4 -5
"""
count = 0
while count < 4:
    print(count)
    count += 1

count = 2
while count < 7:
    print(count)
    count += 1

count = 1
while count < 8:
    print(count)
    count += 2

count = 8
while count > 3:
    print(count)
    count += -1

count = -1
while count > -6:
    print(count)
    count += -1
