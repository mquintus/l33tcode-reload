# 951 - Flip Equivalent Binary Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def isFlippy(node1, node2):
            if node1 is None and node2 is None: return True
            if node1 is None: return False
            if node2 is None: return False
            if not node1.val == node2.val: return False

            if node1.left is None and node2.left is None and node1.right is None and node2.right is None:
                return True

            return ((isFlippy(node1.left, node2.left) and isFlippy(node1.right, node2.right))
                or  (isFlippy(node1.right, node2.left) and isFlippy(node1.left, node2.right)))
        return isFlippy(root1,root2)
            
