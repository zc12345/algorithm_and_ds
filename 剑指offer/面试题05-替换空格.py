class Solution:
    def replaceSpace(self, s: str) -> str:
        s1 = ''
        for i, e in enumerate(s):
            if e == ' ':
                s1 += '%20'
            else:
                s1 += e
        return s1