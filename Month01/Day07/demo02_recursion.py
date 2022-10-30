# 递归 recursion

# 计算数学：阶乘
# 5! = 5 * 4 * 3 * 2 * 1  --> 5! = 5 * 4!
# 4! = 4 * 3 * 2 * 1      --> 4! = 4 * 3!
# 3! = 3 * 2 * 1          --> 3! = 3 * 2!
# 2! = 2 * 1              --> 2! = 2 * 1!
# 1! = 1

# def factor(n):
#     if n == 1:
#         return 1
#     return n * factor(n-1)
#
# print(factor(5))


# 异常：达到最大的深度错误: RecursionError: maximum recursion depth exceeded
import sys

def factor(n):
    return n * factor(n-1)

print(sys.getrecursionlimit())   # 获取系统设置的最大递归深度值
sys.setrecursionlimit(1200)      # 设置系统设置的最大递归深度值（了解）
print(sys.getrecursionlimit())
print(factor(5))

'''
    递归函数总结
        1 清楚 递推 + 回归
        2 结束条件
'''