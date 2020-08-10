from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sort_nums = list(sorted(nums))
        l, r = 0, len(nums) - 1
        print(sort_nums, nums)
        while l < r and (sort_nums[l] == nums[l] or sort_nums[r] == nums[r]):
            print(l, r)
            if sort_nums[l] == nums[l]:
                l += 1
            if sort_nums[r] == nums[r]:
                r -= 1
        # print(sort_nums, l, r)
        return r-l+1


if __name__ == "__main__":
    num = [2, 6, 4, 8, 10, 9, 15]
    Solution().findUnsortedSubarray(num)
