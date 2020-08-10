#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#
from collections import Counter
# @lc code=start


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        last, curr = 0, 1
        for i in range(1, n):
            if s[i] == s[i-1]:
                curr += 1
            else:
                last = curr
                curr = 1
            if last >= curr:
                res += 1
        return res

# @lc code=end


if __name__ == "__main__":
    s = '00110011'
    # s = '10101'
    res = Solution().countBinarySubstrings(s)
    print(res)
