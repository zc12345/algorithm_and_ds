#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start


class Solution:
    def myAtoi(self, str: str) -> int:
        res = ''
        i = 0
        flag = True
        if not str:
            return 0
        str = str.lstrip()
        if i < len(str):
            if str[i] == '-':
                flag = False
                i += 1
            elif str[i] == '+':
                i += 1
            elif not str[i].isdigit():
                return 0

        while i < len(str):
            if str[i].isdigit():
                res += str[i]
            else:
                break
            i += 1
        if len(res) == 0:
            return 0
        ans = int(res) if flag else - int(res)
        if ans < -2 ** 31:
            ans = -2 ** 31
        elif ans > 2 ** 31 - 1:
            ans = 2**31 - 1
        return ans

# @lc code=end


if __name__ == "__main__":
    case = ["-+1", '-', '+1', ' -123x', "-91283472332"]
    for c in case:
        r = Solution().myAtoi(c)
        print(r)
