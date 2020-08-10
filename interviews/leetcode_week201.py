class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = ['0']
        shift = 0
        for i in range(1, n):
            curr = int(s[-1], 2)
            shift = len(s[-1])
            rev = (2**shift-1) ^ curr
            rev = '{:b}'.format(rev)
            padding = shift - len(rev)
            rev = '0'*padding + rev
            rev = rev[::-1]
            tmp = (curr << (shift+1)) + (1 << shift) + int(rev, 2)
            tmp = bin(tmp)[2:]
            padding = shift*2+1-len(tmp)
            tmp = '0'*padding + tmp
            s.append(tmp)
        print(s)
        res = s[-1]
        return res[k-1]

    def makeGood(self, s: str) -> str:
        if not s:
            return s
        while not (s.islower() and s.isupper()) and len(s) > 1:
            i, n = 0, len(s)
            while i < n-1:
                if s[i].islower() and s[i+1] == s[i].upper() or s[i].isupper() and s[i+1] == s[i].lower():
                    s = s[:i]+s[i+2:]
                    print(s)
                    break
                i += 1
            if i == n - 1:
                break
        return s


if __name__ == "__main__":
    so = Solution()
    res = so.makeGood("Pp")
    print(res)
    # n = 4
    # k = 11
    # res = Solution().findKthBit(n, k)
    # print(res)
