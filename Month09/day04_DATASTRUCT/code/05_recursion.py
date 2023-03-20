"""
  递归
"""
# 计算 n + (n-1) + (n-2) + ... + 1 的和


def f(n):
    if n == 1:
        return 1

    return n + f(n-1)


print(f(998))








