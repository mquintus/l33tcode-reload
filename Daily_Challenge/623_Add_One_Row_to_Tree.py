# 623 - Add One Row to Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        def recursive(root, val, depth):
            if root is None:
                return
            
            if depth == -1:
                leftNode = TreeNode(val, root)
                return leftNode
            
            if depth == 0:
                root = insert_children(root, val)
                return root
            
            recursive(root.left, val, depth-1)
            recursive(root.right, val, depth-1)
            return root
            
        def insert_children(root, val):
            leftNode = TreeNode(val, root.left)
            root.left = leftNode
            
            rightNode = TreeNode(val, None, root.right)
            root.right = rightNode
            return root
        root = recursive(root, val, depth-2)
        return root
