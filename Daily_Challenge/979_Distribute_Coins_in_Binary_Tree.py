# 979 - Distribute Coins in Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        absCount = [0]

        def recursiveFunction(node):
            if node is None:
                return 0
            l, r = recursiveFunction(node.left), recursiveFunction(node.right)
            absCount[0] += abs(l) + abs(r)
            #print(absCount)
            return (node.val - 1) + l + r

        recursiveFunction(root)
        return absCount[0]
