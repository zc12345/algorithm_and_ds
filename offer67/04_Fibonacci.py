'''
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。

n<=39 
'''

# -*- coding:utf-8 -*-


class Solution:
    def Fibonacci(self, n):
        # write code here
        Fib = [0, 1]
        for i in range(2, n+1):
            f = Fib[i - 1] + Fib[i - 2]
            Fib.append(f)
        return Fib[n]

    def Fibonacci1(self, n):
        # write code here
        if n < 2:
            return n
        else:
            return self.Fibonacci1(n - 1) + self.Fibonacci1(n - 2)

    def Fibonacci2(self, n):
        x, y = 0, 1
        while n > 0:
            x = x + y
            y, x = x, y
            n -= 1
        return x


if __name__ == "__main__":
    for i in range(10):
        print(Solution().Fibonacci2(i))
