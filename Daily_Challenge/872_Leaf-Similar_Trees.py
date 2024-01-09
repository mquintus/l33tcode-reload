# 872 - Leaf-Similar Trees
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_next_leaf(root):
            if root.left is None and root.right is None:
                yield root.val
            if root.left is not None:
                yield from get_next_leaf(root.left)
            if root.right is not None:
                yield from get_next_leaf(root.right)
        
        iter1 = get_next_leaf(root1)
        iter2 = get_next_leaf(root2)

        while True:
            a = None
            b = None
            try: 
                a = next(iter1)
            except: 
                pass
            try:
                b = next(iter2)
            except:
                pass
            if a is None and b is None:
                return True
            if a is None:
                return False
            if b is None:
                return False
            if a != b: 
                return False
        
