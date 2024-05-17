# 1325 - Delete Leaves With a Given Value
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def recursiveFunction(node):
            if node is None:
                return None

            node.left = recursiveFunction(node.left)
            node.right = recursiveFunction(node.right)
            if node.left or node.right:
                return node

            # This is a leaf node
            if node.val == target:
                return None
            return node
           
        return recursiveFunction(root)
