#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
from typing import List
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]

# @lc code=end


if __name__ == "__main__":
    cases = [
        [3, 2, 1, 5, 6, 4],
        [3, 2, 3, 1, 2, 4, 5, 5, 6]
    ]
    ks = [2, 4]
    labels = [5, 4]
    solution = Solution()
    for i, case in enumerate(cases):
        k = ks[i]
        label = labels[i]
        res = solution.findKthLargest(case, k)
        print(res, label)
