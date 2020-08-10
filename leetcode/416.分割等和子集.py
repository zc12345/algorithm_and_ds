#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        values = sum(nums)
        if values % 2 == 1:
            return False
        half = values // 2
        dp = [0] * (half+1)
        for v in nums:
            for i in range(half, v-1, -1):
                dp[i] = max(dp[i], dp[i-v]+v)
        return half == dp[-1]

# @lc code=end


if __name__ == "__main__":
    # values = [1, 5, 11, 5]
    values = [1, 2, 3, 5]
    res = Solution().canPartition(values)
    print(res)
