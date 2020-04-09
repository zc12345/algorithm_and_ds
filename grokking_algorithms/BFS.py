#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  BFS.py
@Time          :  2020/03/04 01:28:44
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  breadth first search
'''

from collections import deque

def dfs_search(graph, s):
    visited_nodes = set()
    stack = []
    visited_nodes.add(s)
    stack.append(s)
    while stack:
        node = stack.pop()
        for n in graph[node]:
            if n not in visited_nodes:
                stack.append(node)
                stack.append(n)
                visited_nodes.add(n)
                print(n)
                break

def bfs_search(graph, name):
    search_queue = deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if check(person):
                print(person, 'is searched.')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def check(name):
    if name[-1] == 'm':
        return True


if __name__ == "__main__":
    
    # graph={
    #     'A':['B','C'],
    #     'B':['D','E','A'],
    #     'C':['F','G','A'],
    #     'D':['B','H','I'],
    #     'E':['B'],
    #     'F':['C'],
    #     'G':['C'],
    #     'H':['D'],
    #     'I':['D']
    # }
    # s = 'A'
    # dfs_search(graph, s)
    # dfs(graph, s)
    graph = {}  # 使用hash表构建graph
    graph['you'] = ['alice', 'bob', 'claire']
    graph['bob'] = ['anuj', 'peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['tom', 'john']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['tom'] = []
    graph['john'] = []

    name = 'you'
    # res = bfs_search(graph, name)
    res = dfs_search(graph, name)
    # print(res)
