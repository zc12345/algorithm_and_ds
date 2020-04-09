#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File          :  binary_tree_traversal.py
@Time          :  2020/03/08 00:59:03
@Author        :  zc12345 
@Version       :  1.0
@Contact       :  2104158177@qq.com
@Description   :  None

前序遍历 pre_order
中序遍历 in_order
后序遍历 post_order
'''

class BinaryTreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def visit(root, arr):
    arr.append(root.val)


def pre_order_recu(root, arr=[]):
    if root is None:
        return
    visit(root, arr)
    pre_order_recu(root.left, arr)
    pre_order_recu(root.right, arr)
    return arr

def in_order_recu(root, arr=[]):
    if root is None:
        return
    in_order_recu(root.left, arr)
    visit(root, arr)
    in_order_recu(root.right, arr)
    return arr

def post_order_recu(root, arr=[]):
    if root is None:
        return
    post_order_recu(root.left, arr)
    post_order_recu(root.right, arr)
    visit(root, arr)
    return arr


if __name__ == "__main__":
    root=BinaryTreeNode(0)
    node1=BinaryTreeNode(1)
    node2=BinaryTreeNode(2)
    node3=BinaryTreeNode(3)
    node4=BinaryTreeNode(4)
    node5=BinaryTreeNode(5)
    node6=BinaryTreeNode(6)
    node7=BinaryTreeNode(7)
    node8=BinaryTreeNode(8)
    node9=BinaryTreeNode(9)
    root.left, root.right = node1, node2
    node1.left, node1.right = node3, node4
    node2.left, node2.right = node5, node6
    node3.left, node3.right = node7, node8
    node4.left = node9
    arr1 = pre_order_recu(root)
    arr2 = in_order_recu(root)
    arr3 = post_order_recu(root)
    print(arr1, arr2, arr3)
