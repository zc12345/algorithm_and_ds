#
# @lc app=leetcode.cn id=114 lang=python3
#
# [114] 二叉树展开为链表
#
from typing import List
# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return None
        self.flatten(root.left)
        self.flatten(root.right)
        tmp = root.right
        root.right = root.left
        root.left = None
        while root.right:
            root = root.right
        root.right = tmp


# @lc code=end

if __name__ == "__main__":
    nodes = [TreeNode(i) for i in range(1, 7)]
    root = nodes[0]
    root.left, root.right = nodes[1], nodes[4]
    root.left.left, root.left.right = nodes[2], nodes[3]
    root.right.right = nodes[5]
    res = Solution().flatten(root)
    while res:
        print(res.val)
        res = res.right
