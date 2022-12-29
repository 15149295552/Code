'''
2. 学生分数最小差值给你一个 下标从 0 开始 的整数数组nums ，其中 nums[i] 表示第 i 名学生的分数。另给你一个整数 k 。从数组中选出任意 k 名学生的分数，使这 k 个分数间 最高分和 最低分 的 差值 达到 最小化 。返回可能的 最小差值 。
'''
from typing import List


def minNumDifference(nums: List[int], k: int) -> int:
    '''
        计算指定个数的列表元素的最大与最小的差值
    :param nums: 存储整型元素的列表
    :param k: 个数
    :return: 差值的最小值
    '''
    # 1 对 nums 排升序
    nums.sort()

    # 2 获取nums的长度值
    n = len(nums)

    # 3 如果长度值等于个数，直接使用最大值减去最小值
    if n == k:
        return nums[-1] - nums[0]

    # 4 通过循环控制，获取最大值与最小值之间的差值
    m = 10 ** 7

    # 实例：[1, 2, 4, 6, 8]   3   # 相邻元素之间的差值最小
    for i in range(n - k + 1):
        # 判断k个元素中最后1个元素与第1个元素的差值比较
        if nums[k + i - 1] - nums[i] < m:
            # 如果差值小于上一次的，给m重新赋值
            m = nums[k + i - 1] - nums[i]
    return m


print(minNumDifference([1, 2, 4, 6, 8], 3))
print(minNumDifference([90], 1))
print(minNumDifference([9, 4, 1, 7], 2))
