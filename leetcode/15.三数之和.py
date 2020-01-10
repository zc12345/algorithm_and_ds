#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, n1 in enumerate(nums):
            if n1>0:
                break
            elif i>0 and n1 == nums[i-1]:
                continue
            left, right = i+1, len(nums)-1
            while left<right:
                n2, n3 = nums[left], nums[right]
                s = n1 + n2 + n3
                if s == 0:
                    r = [n1, n2, n3]
                    res.append(r)
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                        pass
                    left += 1
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    right -= 1
        return res
# @lc code=end

