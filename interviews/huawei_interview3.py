#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  huawei_interview3.py
@Time          :  2020/06/24 20:36:38
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  有向图的最短路径问题（Dijkstra算法）

某旅游景区有n个景点,编号从1到n,其中景点1还是游客集散中心,景点之间相隔较远,有2n-2条单向车道连接,编号从1到2n-2,车道可以分为两大类:
1.前n-1条单向车道会组成一个以景点1 (集散中心)为根的生成树(根节点直达任何节点,部分直达,部分通过其他节点跳转可达),方便从集散中心到达各个景点.
2.后n-1条单向车道从景点i向景点1 (集散中心) ,其中2<=i<=n,也就是其他节点都可以直达根节点,方便用户随时从各景点返回。

现在需开发一个系统用于实时查询两个景点之间的最短距离,系统支持两种操作命令:
1.操作命令为[1 i w], 1表示修改操作,表示将第i条车道的长度调整为w
2.操作命令为[2 u v], 2表示查询操作,表示打印景点u到景点v的最短路径
根据所有的操作命令,打印所有查询操作的结果
'''


class Solution:
    def __init__(self, n, q, root, operater):
        self.n = n
        self.q = q
        self.root = root
        self.operater = operater
        self.matrix = [[99999999 for i in range(n)] for j in range(n)]
        for cur_root in root:
            self.matrix[cur_root[0]-1][cur_root[1]-1] = cur_root[2]
        self.operater = operater

    def chagematrix(self, root):
        self.matrix = [[99999999 for i in range(n)] for j in range(n)]
        for cur_root in root:
            self.matrix[cur_root[0]-1][cur_root[1]-1] = cur_root[2]

    def dijkstra(self, source_node, target):
        inf = float('inf')
        # init the source node distance to others
        dis = self.matrix[source_node]
        node_nums = len(dis)

        flag = [0 for i in range(node_nums)]
        flag[source_node] = 1

        for i in range(node_nums - 1):
            min = inf
            for j in range(node_nums):
                if flag[j] == 0 and dis[j] < min:
                    min = dis[j]
                    u = j
            flag[u] = 1
            for v in range(node_nums):
                if flag[v] == 0 and self.matrix[u][v] < inf:
                    if dis[v] > dis[u] + self.matrix[u][v]:
                        dis[v] = dis[u] + self.matrix[u][v]
        return dis[target]

    def pprint(self):
        res = []
        for i in range(self.q):  # 根据所有操作命令，打印所有查询操作的结果
            if self.operater[i][0] == 1:
                root[self.operater[i][1]-1][2] = self.operater[i][2]
                self.chagematrix(root)
            elif self.operater[i][0] == 2:
                res.append(self.dijkstra(
                    operater[i][1] - 1, operater[i][2] - 1))
        return res


class Solution2:
    def __init__(self, n, q, root, operater):
        self.road1 = root[: n - 1]
        self.road2 = root[n - 1:]
        self.operater = operater

    def fun(self, road1):
        road = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n - 1):
            road[road1[i][0]][road1[i][1]] = road1[i][2]
        for i in range(2, n+1):
            length = 0
            index = i
            while(1):
                for j in range(1, n+1):
                    if road[j][index] != -1:
                        length += road[j][index]
                        index = j
                        if index == 1:
                            break
                if index == 1:
                    break
            road[1][i] = length
        return road

    def pprint(self):
        road1 = self.road1
        road2 = self.road2
        road = self.fun(road1)
        oper = self.operater
        res = []
        for i in range(q):
            if oper[i][0] == 1:
                road1[oper[i][1]-1][2] = oper[i][2]
                road = self.fun(road1)
            else:
                if road[oper[i][1]][oper[i][2]] != -1:
                    res.append(road[oper[i][1]][oper[i][2]])
                else:
                    res.append(road[1][oper[i][2]] + road2[oper[i][1] - 2][2])
        return res


if __name__ == '__main__':
    n, q = 6, 6  # n景点个数，q操作命令个数
    matrices = [
        [1, 3, 4],  # [a_i, b_i, c_i] 景点a_i到b_i的距离为c_i
        [3, 2, 5],
        [1, 4, 6],
        [4, 5, 2],
        [4, 6, 3],
        [2, 1, 3],
        [3, 1, 4],
        [4, 1, 3],
        [5, 1, 5],
        [6, 1, 2],  # 前2n-2行，表示所有单向车道
        [2, 1, 5],
        [2, 6, 5],
        [1, 4, 3],
        [2, 1, 6],
        [2, 6, 5],
        [2, 3, 5]  # 后q行，表示q个操作命令
    ]
    expected = [8, 10, 9, 11, 13]
    res = []
    root = matrices[: 2 * n - 2]
    operater = matrices[2 * n - 2:]
    solution = Solution(n, q, root, operater)
    res = solution.pprint()
    print(res == expected)
