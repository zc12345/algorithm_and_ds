'''
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 

 

限制：

2 <= n <= 100000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

题解：
只是时间优先就用字典，
还有空间要求，就用指针+原地排序数组，
如果面试官要求空间O(1)并且不能修改原数组，还得写成二分法！！！
'''
from typing import List

class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums.sort() 
        pre = nums[0]
        for e in nums[1:]:
            if e == pre:
                return e
            pre = e 
            
    def findRepeatNumber2(self, nums: List[int]) -> int:
        repeatDict = {}
        for e in nums:
            if e not in repeatDict:
                repeatDict[e] = 1
            else:
                return e

if __name__ == "__main__":
    res = Solution().findRepeatNumber([2, 3, 1, 0, 2, 5, 3])
    print(res)