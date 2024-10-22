# 2583 - Kth Largest Sum in a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        levels = []
        def rec(node, depth):
            if len(levels) < depth + 1:
                levels.append(0)
            levels[depth] += node.val
            if node.left is not None:
                rec(node.left, depth+1)
            if node.right is not None:
                rec(node.right, depth+1)
        rec(root, 0)
        if len(levels) < k: return -1
        levels.sort()
        return levels[-k]
