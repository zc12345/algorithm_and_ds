#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  DFS.py
@Time          :  2020/03/07 16:58:22
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  depth first search algorithm
'''

from collections import deque


class Node():
    def __init__(self, x):
        self.val = x
        self.neighbors = None


def dfs_search(root):
    visited_nodes = set()
    stack = []
    visited_nodes.add(root)
    stack.append(root)
    while stack:
        curr = stack.pop()
        for node in curr.neighbors:
            if node not in visited_nodes:
                stack.append(curr)
                stack.append(node)
                visited_nodes.add(node)
                print(node.val)
                break

def dfs_search_rec(node, visited_nodes=set()):
    if node is None:
        return
    visited_nodes.add(node)
    print(node.val)
    for n in node.neighbors:
        if n not in visited_nodes:
            dfs_search_rec(n, visited_nodes)

def bfs_search(root):
    queue = deque()
    queue.append(root)
    visited_nodes = set()
    visited_nodes.add(root)
    while queue:
        curr = queue.popleft()
        for n in curr.neighbors:
            if n not in visited_nodes:
                queue.append(n)
                visited_nodes.add(n)
                print(n.val)


if __name__ == "__main__":
    root=Node(0)
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    node5=Node(5)
    node6=Node(6)
    node7=Node(7)
    node8=Node(8)
    node9=Node(9)
    root.neighbors=[node1, node2, node3]
    node1.neighbors=[node4, node5, root]
    node2.neighbors=[node6, node7, root]
    node3.neighbors=[node8, node9, root]
    node4.neighbors=[node1]
    node5.neighbors=[node1]
    node6.neighbors=[node2]
    node7.neighbors=[node2]
    node8.neighbors=[node3]
    node9.neighbors=[node3]
    bfs_search(root)
    dfs_search(root)
    dfs_search_rec(root)
