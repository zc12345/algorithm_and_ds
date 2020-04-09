'''
2020/03/23
阿里笔试题1(内存和时间都达不到要求，应该有别的解法)
现有n个人，要从这n个人中选任意数量的人组成一支队伍，再在这支队伍中选出一名队长，求不同的方案数对(10^9+7)取模的结果。
如果两个方案选出的队长不同，则认为是不同的两个方案。
输入描述：1 <= n <= 10^9
例：
输入：2
输出：4 ((_1), (_2), (_1, 2), (1, _2))

阿里笔试题2
小强在玩一个走迷宫的游戏，他操纵的人物现在位于迷宫的起点，他的目标是尽快到达终点。
每一次他可以选择花费一个时间单位向上或向下或向左或向右走一格，或是使用自己的对称飞行器花费一个时间单位瞬移到关于当前自己点中心对称的格子，且每次移动的目的地不能存在障碍物。
具体来说，设当前迷言有n行m列，如果当前小强操控的人物位于点A(x,y),那么关于点A中心对称的格子B(x',y');满足x+x'=n+1且y+y'=m+1。
需要注意的是，对称飞行器最多使用5次。
输入描述:
第一行两个空格分隔的正整数n,m， 分别代表迷宫的行数和列数。
接下来n行每行一个长度为m的字符串来描述这个迷宫。
其中N代表通路。#代表障碍。S代表起点。E代表终点。保证只有一个S和一个E。2< n,m < 500
输出描述:
仅一行一个整数表示从起点最小花费多少时间单位到达终点。如果无法到达终点，输出-1。
例：
输入：
4 4
#S..
E#..
#...
....
输出：4
说明：一种可行的路径是用对称飞行器到达(4, 3)再向上走一步，再向右走一步，然后使用一次对称飞行器到达终点
'''
def solution1(n):
    n_dict = [1 for i in range(n+1)]
    res = 0
    for i in range(1, n+1):
        n_dict[i] = i * n_dict[i - 1] % (10**9 + 7)
    # print(n_dict)
    for k in range(1, n+1):
        tmp = k * n_dict[n] // n_dict[k] // n_dict[n - k] % (10**9 + 7)
        # print(tmp)
        res += tmp
    print(res% (10**9 + 7))
    return res

if __name__ == "__main__":
    solution1(100)