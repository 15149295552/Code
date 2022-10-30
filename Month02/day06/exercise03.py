"""
外层循环 4 次  内层循环
$                1
$$               2
$$$              3
$$$$             4
"""
for r in range(4):  # 0  1   2    3
    for c in range(r + 1):  # 0  01  012  0123
        print("$", end="")
    print()
