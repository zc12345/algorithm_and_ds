#
# @lc app=leetcode.cn id=95 lang=python3
#
# [95] 不同的二叉搜索树 II
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
    def generateTrees(self, n: int) -> List[TreeNode]:
        res = []
        if n < 1:
            return res
        else:
            return self.generateBST(1, n)

    def generateBST(self, start, end):
        res = []
        if start > end:
            res.append(None)
            return res
        else:
            for i in range(start, end+1):
                left_tree = self.generateBST(start, i-1)
                right_tree = self.generateBST(i+1, end)
                for left in left_tree:
                    for right in right_tree:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        res.append(root)
            return res

# @lc code=end


if __name__ == "__main__":
    n = 3
    res = Solution().generateTrees(n)
    print(res)
