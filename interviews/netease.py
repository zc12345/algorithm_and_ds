import bisect
from collections import defaultdict, Counter, deque


class TreeNode:
    def __init__(self, val=None, child=[], parent=None):
        self.val = val
        self.child = child
        self.parent = parent

#
#
# @param node_data_list int整型二维数组
# @return int整型二维数组
#


class Solution1:
    # def __init__(self, node_list):
    #     if not node_list:
    #         return
    #     self.node_list = node_list
    #     self.root = TreeNode(node_list[0][0], [], TreeNode(node_list[0][1]))
    #     self.return_list = []

    def search(self, val, list):
        return_list = []
        for i in range(len(list)):
            if list[i][1] == val:
                return_list.append(list[i])
        return return_list

    def dfs(self, node):
        if not node:
            return
        self.return_list.append([node.val, node.parent.val])
        node.child = node.child[::-1]
        for i in range(len(node.child)):
            self.dfs(node.child[i])

    def invert_tree(self, node_data_list):
        # write code here
        if not node_data_list:
            return []
        self.node_list = node_data_list
        self.root = TreeNode(
            node_data_list[0][0], [], TreeNode(node_data_list[0][1]))
        self.return_list = []
        nodeL = [self.root]
        while nodeL:
            cur_node = nodeL.pop(0)
            cur_val = cur_node.val
            child_val_list = self.search(cur_val, self.node_list)
            for i in range(len(child_val_list)):
                child_node = TreeNode(child_val_list[i][0], [], cur_node)
                cur_node.child.append(child_node)
                nodeL.append(child_node)
        self.dfs(self.root)
        return self.return_list


class Solution2:
    def city(self, edges, use_case, m, n):
        citys = []
        G = [[] for _ in range(n+1)]
        # print(G)
        # print(edges)
        for e1, e2 in edges:
            # print(e1, e2)
            G[e1].append(e2)
            G[e2].append(e1)

        node_to_level = {}
        visited = [0 for _ in range(n+1)]
        Q1 = deque()
        Q1.append(1)
        visited[1] = 1

        level = 1
        while len(Q1) > 0:
            cur_cnt = len(Q1)
            for _ in range(cur_cnt):
                node = Q1.popleft()
                node_to_level[node] = level
                for son in G[node]:
                    if visited[son] == 0:
                        visited[son] = 1
                        Q1.append(son)
            level += 1
        for i in range(len(use_case)):
            start, end = use_case[i][0], use_case[i][1]
            max_level = n+1
            res = start
            need_city = end - start + 1
            match_city = 0
            visited = [0 for _ in range(n+1)]
            Q2 = deque()
            Q2.append((start, start))
            visited[start] = 1

            while len(Q2) > 0:
                node, max_city = Q2.popleft()
                node_level = node_to_level[node]

                if start <= node <= end:
                    match_city += 1
                    if node_to_level[max_city] < max_level:
                        max_level = node_to_level[max_city]
                        res = max_city

                if match_city == need_city:
                    break

                for son in G[node]:
                    if visited[son] == 0:
                        visited[son] = 1

                        which_city = max_city
                        if node_to_level[max_city] > node_to_level[son]:
                            which_city = son
                        Q2.append((son, which_city))

            citys.append(res)
        return citys


#
# 根据给定的数据，确定病毒的类型
# @param size int整型 基因片段数量，取值范围: 2 到 1e6
# @param swap_indexes int整型二维数组 酶处理时，交换的基因片段的位置。
# swap_indexes[n][0] != swap_indexes[n][1] 一定成立。行数取值范围：[1, 1e6], 列数衡为2
# @return int整型
#


class Solution3:
    def determine_virus_type(self, size, swap_indexes):
        # write code here
        gene = [size-i for i in range(size)]

        for i, j in swap_indexes:
            gene[i], gene[j] = gene[j], gene[i]
        sorted_nums = []
        res = 0
        for n in gene:
            index = bisect.bisect_left(sorted_nums, n)
            bisect.insort(sorted_nums, n)
            res += index
        return 1 if res % 2 != 0 else 2

#
#
# @param filenames string字符串一维数组 所有文件名
# @param relations string字符串二维数组 文件依赖关系
# @return int整型
#


class Solution4:
    def split_package(self, filenames, relations):
        # write code here
        maps = {item: item for item in filenames}

        def find(x):
            if maps[x] != x:
                maps[x] = find(maps[x])
            return maps[x]

        def union(x, y):
            x = find(x)
            y = find(y)
            if x > y:
                maps[x] = y
            elif x < y:
                maps[y] = x

        for item in relations:
            union(item[0], item[1])
        for item in filenames:
            find(item)
        return len(set(maps.values()))


if __name__ == "__main__":
    # ins = [[1, 0], [2, 1], [3, 1]]
    # expect = [[1, 0], [3, 1], [2, 1]]
    # res = Solution1().invert_tree(ins)
    # print(res)
    # print(res == expect)
    ins1 = [[1, 2], [1, 3], [2, 4], [5, 2], [2, 6], [3, 7], [8, 3], [3, 9]]
    ins2 = [[4, 5], [5, 7], [7, 9]]
    m, n = 3, 9
    res = Solution2().city(ins1, ins2, m, n)
    expect = [2, 1, 3]
    print(res == expect)

    # size = 5
    # swap_indexes = [[2, 4], [1, 4], [0, 3], [0, 3]]
    # expect = 2
    # res = Solution3().determine_virus_type(size, swap_indexes)
    # print(res == expect)
    # filenames = ["fileA", "fileB", "fileC", "fileD", "fileE"]
    # relations = [["fileA", "fileB"], ["fileB", "fileC"], ["fileD", "fileE"]]
    # expect = 2
    # res = Solution4().split_package(filenames, relations)
    # print(res == expect)
