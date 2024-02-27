# 543 - Diameter of Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def solve(root):
            if root is None:
                return 0
            return max(
                solve(root.left),
                solve(root.right),
                depth(root.left) + depth(root.right)
            )

        def depth(root):
            if root is None:
                return 0
            return 1 + max(depth(root.left), depth(root.right))

        #print(
        #        solve(root.left),
        #        solve(root.right),
        #        depth(root.left), 
        #        depth(root.right)
        #    )

        return solve(root)
