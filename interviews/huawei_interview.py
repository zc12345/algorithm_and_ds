'''
华为2020/06/17 题目3

定义一种数字集合的加法和乘法：
[1,2,3]表示一个有三个数字的集合
[1,2,3],[2,4]表示集合之间相加，其结果取并集为[1,2,3,4]
相乘有三种形式：
4[1,2,3] 其结果为[41,42,43]
[0,1,2]4 其结果为[4,14,24]
[1,2,3][4,5] 其结果为[14,15,24,25,34,35]
允许集合之间运算的嵌套，如：
[[1,2],[2,3]]4[5,6] = [1,2,3][45,46] = [145,146,245,246,345,346]
给出基于这种集合运算的表达式，返回结果的有序列表，且结果中不能有重复的数字
1. 题目保证最后运算出的数字不会超过2.1e9
2. 运算优先级[]>乘法>加法
'''

import collections


class Solution(object):
    def getResult(self, s_input):
        stack = collections.deque()
        length = len(s_input)
        prev = ''
        i = 0
        while i < length:
            if s_input[i].isdigit():
                stack.append(int(s_input[i]))
                i += 1
                continue
            if s_input[i] == ',' or ((not stack) and s_input[i] == '['):
                i += 1
                continue
            l = len(stack)
            flag = 0
            i += 1
            while i < length and s_input[i] != ']' and s_input[i] != '[':
                if s_input[i].isdigit():
                    flag = 1
                    prev = s_input[i]
                    for j in range(l):
                        stack.append(stack[j]*10+int(prev))
                i += 1
            if flag == 0:
                continue
            for _ in range(l):
                stack.popleft()
        return sorted(set(stack))
        # res = []
        # print(sorted(set(stack)))
        # for i in stack:  # 去重
        #     if i not in res:
        #         res.append(i)
        # return sorted(res)


if __name__ == "__main__":
    case1 = '[1,2][3[4,5]]'
    case2 = '[0,1]2'
    case3 = '[1,2,3][4,5]'
    case4 = '4[1,2,3]'
    res = Solution().getResult(case4)
    print(res)
