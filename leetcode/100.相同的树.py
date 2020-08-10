#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        elif not p or not q:
            return False
        elif p.val != q.val:
            return False
        else:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

# @lc code=end


if __name__ == "__main__":
    nodes = [TreeNode(i) for i in range(10)]
    root = nodes[0]
    root.left, root.right = nodes[1], nodes[2]
    root.left.left, root.left.right = nodes[3], nodes[4]
    root.right.left, root.right.right = nodes[5], nodes[6]
    root2 = nodes[7]
    res = Solution().isSameTree(root, root2)
    print(res)
