# coding=utf8
'''
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''
from typing import List
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = 0
        b = 0
        l = len(nums)
        for i in range(l):
            for j in range(i+1,l):
                s = nums[i]+nums[j]
                if s==target:
                    a = i
                    b = j
                    return [a,b]

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for index, num in enumerate(nums):
            if target - num in d:
                k = d[target - num]
                return [k,index]
            d[num] = index

class Solution3:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            d[num] = i
        for i, num in enumerate(nums):
            if target - num in d and not(i == d[target-num]):
                return [i,d[target - num]]
        return [-1,-1]

class Solution4:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        l = len(nums)
        for j in range(l):
            if target - nums[j] in d:
                return [d[target - nums[j]], j]
            d[nums[j]] = j
        return [-1,-1]

    
if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    res = Solution4().twoSum(nums, target)
    print(res)
