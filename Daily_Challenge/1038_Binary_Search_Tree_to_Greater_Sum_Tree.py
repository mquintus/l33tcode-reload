# 1038 - Binary Search Tree to Greater Sum Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def getVal(root, val=0):
            if root.right:
                val = getVal(root.right, val)
            
            root.val += val
            val = root.val
            
            if root.left:
                val = getVal(root.left, val)
            
            return val
        
        getVal(root)
        return root
