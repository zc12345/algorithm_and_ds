# coding=utf8
'''
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        left = cnt = 0
        s_set = set(s)
        for left, var in enumerate(s):    
            right = len(s_set) + 5 if len(s)>100 else len(s)+1
            while right - left > cnt:
                sub = s[left:right]
                sub_set = set(sub)
                if len(sub_set) == len(sub) and cnt < len(sub):
                    cnt = len(sub)
                right -= 1
        return cnt

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub = []
        left = right = cnt = 0
        s_set = set(s)
        sub_set = set([])
        while left < len(s) and right < len(s):
            if not s[right] in sub_set:
                sub_set.add(s[right])
                cnt = max(cnt, len(sub_set))
                right += 1
            else:
                sub_set.discard(s[left])
                left += 1
        return cnt
    
class Solution3:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = right = cnt = 0
        sub_dict = {}
        for right in range(len(s)):
            if s[right] in sub_dict:
                left = max(sub_dict[s[right]] , left)
            sub_dict[s[right]] = right + 1
            cnt = max(cnt, right - left + 1)
        return cnt


if __name__ == '__main__':
    s = "pwwkew"
    res = Solution3().lengthOfLongestSubstring(s)
    print(res)

    


    
