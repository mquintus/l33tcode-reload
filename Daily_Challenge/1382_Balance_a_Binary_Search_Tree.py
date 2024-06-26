# 1382 - Balance a Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        allnodes = []
        def rec(node):
            if node.left:
                rec(node.left)
            if node.right:
                rec(node.right)
            nonlocal allnodes
            allnodes.append(node.val)

        rec(root)
        allnodes.sort()
        def generate(left, right):
            if left >= right:
                return None
            
            mid = (left + right) // 2
            newroot = TreeNode(
                allnodes[mid],
                generate(left, mid),
                generate(mid+1, right)
            )
            return newroot
        return generate(0, len(allnodes))
