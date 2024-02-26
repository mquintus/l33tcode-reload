# 100 - Same Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        if p is None:
            return False
        if q is None:
            return False

        if p.val != q.val:
            return False
        if p.left and p.right:
            if not q.left or not q.right:
                return False
            if q.left and q.right:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        elif p.left:
            if q.left and q.right:
                return False
            if q.left and not q.right:
                return self.isSameTree(p.left, q.left)
            if not q.left and q.right:
                return False
        elif p.right:
            if not q.right:
                return False
            if q.left:
                return False
            if not q.left and q.right:
                return self.isSameTree(p.right, q.right)
        else:
            if q.left is not None or q.right is not None:
                return False
        return True
                

        
