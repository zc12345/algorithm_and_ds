#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start


class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ''
        for ch in s.lower():
            if ch.isalnum():
                res += ch
        return res == res[::-1]
# @lc code=end
