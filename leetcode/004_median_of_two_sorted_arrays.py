# coding=utf8
'''
4. Median of Two Sorted Arrays
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        curr = 0
        i = j = k = 0
        nums = []
        median = 0
        if len(nums1)==0 and not len(nums2)==0:
            nums = nums2
        elif len(nums2)==0 and not len(nums1)==0:
            nums = nums1
        elif not len(nums2)==0 and not len(nums2)==0:
            while k < len(nums1)+len(nums2):
                if i == len(nums1):
                    curr = nums2[j]
                    j += 1
                elif j == len(nums2):
                    curr = nums1[i]
                    i += 1
                elif nums1[i]<= nums2[j]:
                    curr = nums1[i]
                    i += 1#min(i+1, len(nums1)-1)                    
                else:
                    curr = nums2[j]
                    j += 1#min(j+1, len(nums2)-1)
                nums.append(curr)
                k += 1
        #print(nums)
        median = (nums[int(len(nums)/2-1)]+nums[int(len(nums)/2)])/2 if len(nums)%2==0 else nums[int((len(nums)-1)/2)]
        return median


if __name__ == '__main__':
    a = [1, 3]
    b = [2]
    res = Solution().findMedianSortedArrays(a, b)
    print(res)

    


    
