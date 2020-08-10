import copy
from collections import defaultdict


class Solution1:
    def func(self, values):
        res = 0
        for v in values:
            res += v//2
        return res


class Solution2:
    def func(self, n, a, b):
        dp = [0]*(n+1)
        dp[0], dp[1] = 0, a[0]
        for i in range(2, n+1):
            dp[i] = min(dp[i-2]+b[i-2], dp[i-1]+a[i-1])
        ans = dp[-1]
        s, s_res = ans % 60, ans//60
        m, h = s_res % 60, s_res//60 + 8
        fix = 'am'
        if h > 12:
            fix = 'pm'
        res = '{:0=2}:{:0=2}:{:0=2} {}'.format(h, m, s, fix)
        print(res)


class Solution3:
    def func(self, n, a):
        sums = sum(a)
        maps = {0: 0}
        for x in a:  # 遍历所有东西的价值
            curr = copy.deepcopy(maps)
            for d in curr.keys():  # 遍历已经遍历的东西
                maps[d+x] = max(curr.get(d), maps.get(d+x, 0))
                maps[(abs(d-x))] = max(curr.get(d)+min(d, x),
                                       maps.get(abs(d-x), 0))
            print(maps)
        print(a, sums, maps.get(0))
        return sums - maps.get(0)*2


class Solution4:
    def func(self, n, nums):
        pass


if __name__ == "__main__":
    # values = [5, 3, 7]
    # res = Solution1().func(values)
    # print(res)

    # n = 3
    # a = [20, 25, 30]
    # b = [40, 45]
    # res = Solution2().func(n, a, b)

    a = [30, 60, 5, 15, 30]
    a.sort()
    res = Solution3().func(len(a), a)
    print(res)

    # n = 5
    # a = [
    #     [1, 3],
    #     [2, 1],
    #     [3, 2],
    #     [3, 5],
    #     [4, 5]
    # ]
    # res = Solution4().func(n, a)
