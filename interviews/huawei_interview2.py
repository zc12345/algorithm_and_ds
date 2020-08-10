#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  huawei_interview2.py
@Time          :  2020/06/24 19:35:17
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  
input: 会议开始和结束时间[[start_1, end_1],...,[start_n, end_n]] s.t. 8 <= start_i, end_i <= 23
output:会议室最长使用时间
'''


class Solution:
    def maxTime(self, queue):
        queue.sort(key=lambda pair: pair[1])
        print(queue)
        n = len(queue)
        max_t = 0
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = queue[i][1] - queue[i][0]
        for i in range(1, n):
            t = queue[i][1]-queue[i][0]
            for j in range(i):
                if queue[j][1] <= queue[i][0]:
                    dp[i] = max(dp[j] + t, dp[i])
        return max(dp)


if __name__ == "__main__":
    case = [
        [15, 17], [8, 11], [10, 16], [11, 12], [13, 15], [9, 12]
    ]
    expected = 8
    res = Solution().maxTime(case)
    print(res, expected)
