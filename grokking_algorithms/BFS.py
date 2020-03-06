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


def search(graph, name):
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
    res = search(graph, name)
    print(res)
