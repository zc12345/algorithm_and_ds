#
# @lc app=leetcode.cn id=93 lang=python3
#
# [93] 复原IP地址
#

# @lc code=start
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.res = []

        def backtrack(s, tmp):
            if len(s) == 0 and len(tmp) == 4:
                self.res.append('.'.join(tmp))
                return
            if len(tmp) < 4:
                for i in range(min(3, len(s))):
                    p, n = s[:i + 1], s[i + 1:]
                    if p and 0 <= int(p) <= 255 and str(int(p)) == p:
                        backtrack(n, tmp + [p])

        backtrack(s, [])
        return self.res


# @lc code=end

if __name__ == "__main__":
    s = "25525511135"
    res = Solution().restoreIpAddresses(s)
    print(res)
