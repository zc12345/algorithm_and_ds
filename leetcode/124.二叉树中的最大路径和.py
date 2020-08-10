#
# @lc app=leetcode.cn id=124 lang=python3
#
# [124] 二叉树中的最大路径和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_path = float('-inf')

        def get_max(node):
            if not node:
                return 0
            left = max(0, get_max(node.left))
            right = max(0, get_max(node.right))
            curr_path = left + right + node.val
            self.max_path = max(curr_path, self.max_path)
            return node.val + max(left, right)
        get_max(root)
        return self.max_path
# @lc code=end
