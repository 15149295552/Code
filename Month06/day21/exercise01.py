'''
1. 两个数的和
    给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1]

输入：nums = [3,2,4], target = 6
输出：[1,2]

输入：nums = [3,3], target = 6
输出：[0,1]
'''

# 方法1：使用循环嵌套
''' 
   1 判断列表长度不能小于1
   2 循环1遍历第0个元素到倒数第2个元素： i
   3 循环2遍历第i+1个元素到列表最后一个元素： j
   4 判断第i个元素 + 第j个元素 == 目标值target：返回 [i，j]
'''

# def numberSum(nums, target):
#     '''
#     获取列表中2个元素的和等于目标值target的索引值
#     :params nums: 存储元素的列表
#     :params taget: 目标值
#     :return: 结果等于目标值的元素索引值列表
#     '''
#     if len(nums) > 1:
#         for i in range(len(nums) - 1):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
# 
# 
# print(numberSum([2, 7, 11, 15], 9))
# print(numberSum([3, 2, 4], 6))
# print(numberSum([3, 3], 6))
# print(numberSum([3, 3, 5], 9))



def numberSum(nums, target):
    '''
    获取列表中2个元素的和等于目标值target的索引值
    :params nums: 存储元素的列表
    :params taget: 目标值
    :return: 结果等于目标值的元素索引值列表
    '''
    if len(nums) > 1:
        hashmap = {}
        for index, num in enumerate(nums):
            other = target - num
            if other in hashmap:
                return [hashmap[other], index]
            hashmap[num] = index

print(numberSum([2, 7, 11, 15], 9))
print(numberSum([3, 2, 4], 6))
print(numberSum([3, 3], 6))
print(numberSum([3, 3, 5], 9))