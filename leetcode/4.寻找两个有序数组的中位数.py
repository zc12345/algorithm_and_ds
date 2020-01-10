#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n, A, B = len(nums1), len(nums2), nums1, nums2
        if m > n:
            m, n, A, B = n, m, B, A

        imin, imax, half_len = 0, m, (m+n+1)//2
        while imin <= imin:
            i = (imin + imax)//2 # init: i, j = m//2, (n+1)//2
            j = half_len - i
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                if i == 0: max_of_left = B[j-1]
                elif j == 0: max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])
                if (m+n)%2 == 1:
                    return max_of_left
                if i == m: min_of_right = B[j]
                elif j == n: min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])
                return (max_of_left+min_of_right)/2
        
# @lc code=end

