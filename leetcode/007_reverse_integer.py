# coding=utf8
'''
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2**31,  2**31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''
class Solution:
    def reverse(self, x: int) -> int:
        minx = - 2**31
        maxx = 2**31 - 1
        result = 0
        if x == 0:
            result = 0
        elif x < 0:
            x_str = str(-1 * x)
            result = - 1 * int(x_str[::-1])
        else:
            x_str = str(x)
            result = int(x_str[::-1])
        if result not in range(minx, maxx):
            return 0
        else:
            return result


if __name__ == '__main__':
    s = 123
    res = Solution().reverse(s)
    print(res)

    


    
