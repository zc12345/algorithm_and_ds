# coding=utf8
'''
6. ZigZag Conversion
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I
'''

class Solution1:
    def convert(self, s: str, numRows: int) -> str:
        tmp = []
        res = []
        k = 0
        reverse = True
        if len(s) <= numRows or numRows == 1:
            return s
        for char in s[:numRows]:
            tmp.append(char)
        res.append(tmp)
        tmp = []
        tmp.append('')
        for index, char in enumerate(s[numRows:]):
            tmp.append(char)
            if index == len(s[numRows:]) - 1:
                pad = numRows - len(tmp)
                for i in range(pad):
                    tmp.append('')
            if len(tmp) == numRows:
                if reverse:
                    tmp = tmp[::-1]
                reverse = not reverse
                res.append(tmp)
                
                tmp = []
                tmp.append('')
        final = []
        for i in range(numRows):
            for tmp in res:
                final.append(tmp[i])
        return ''.join(final)

class Solution2:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        n = len(s)
        cycle = 2 * numRows - 2
        res = []
        for i in range(numRows):
            j = 0
            while j < n and j + i < n:
                    res.append(s[i + j])
                    if not i == 0 and not i == numRows - 1 and j + cycle - i < n:
                        res.append(s[j + cycle - i])
                    j += cycle
        return ''.join(res)

class Solution3:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows: return s
        
        rows = ['']*numRows
        curr, down = 0, 0
        for char in s:
            rows[curr] += char
            if curr == 0 or curr == numRows - 1:
                down ^= 1
            curr += 1 if down else  -1
        return ''.join([row for row in rows])

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    res = Solution3().convert(s, numRows)
    print(res)
