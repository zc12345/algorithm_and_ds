#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  Dijkstra_search.py
@Time          :  2020/03/04 01:42:18
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  Dijkstra algorithm to search shortest path
计算 非加权图 最短路径使用 BFS或者DFS
计算 有向无环带权图(DAC, Directed Acyclic Graph) 最短路径使用 Dijkstra算法
计算 有环带权图 最短路径使用 Bellman-Ford算法

Note: 如果有负权重边也不能使用Dijkstra算法

algorithm:
----------------------
repeat for every node:
    1. 找出可在最短时间内前往的节点
    2. 对于该节点的邻居，检查是否有前往他们的更短路径，如果有就更新开销
计算最终路径
'''

def Dijkstra(graph, costs, parents):
    def find_node(costs):
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node
    
    processed = []
    node = find_node(costs)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost=cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_node(costs)
    
if __name__ == "__main__":
    graph = {}
    graph['S'] = {}
    graph['A'] = {}
    graph['B'] = {}
    graph['C'] = {}
    graph['D'] = {}
    graph['fin'] = {}
    graph['S']['A'] = 5
    graph['S']['B'] = 0
    graph['A']['C'] = 15
    graph['A']['D'] = 20
    graph['B']['C'] = 30
    graph['B']['D'] = 35
    graph['C']['fin'] = 20
    graph['D']['fin'] = 10
    
    inf = float('inf')
    costs = {}
    costs['A'] = 5
    costs['B'] = 0
    costs['C'] = inf
    costs['D'] = inf
    costs['fin'] = inf
    
    parents={}
    parents['S'] = None
    parents['A'] = 'S'
    parents['B'] = 'S'
    parents['C'] = None
    parents['D'] = None
    parents['fin'] = None

    Dijkstra(graph, costs, parents)

    print(costs)
    tnode = 'fin'
    path = ['fin']
    while tnode is not None:
        tnode = parents[tnode]
        path.append(tnode)
    path.reverse()
    print(path[1:])
