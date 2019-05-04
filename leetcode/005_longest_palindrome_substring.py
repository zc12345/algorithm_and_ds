# coding=utf8
'''
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub = ""
        left = right = 0
        for left in range(len(s)):
            for right in range(left + len(sub) + 1, len(s)+1):
                s_sub = s[left:right]
                if not s_sub[0] == s_sub[-1]:
                    continue
                reversed_s_sub = ''.join(reversed(s_sub))
                if reversed_s_sub ==s_sub and len(s_sub) > len(sub):
                    sub = s_sub
        return sub


if __name__ == '__main__':
    s = "cbba"
    res = Solution().longestPalindrome(s)
    print(res)

    


    
