# 606 - Construct String from Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def print_traverse(root):
            right = ''
            if root.right is not None:
                right = '(' + print_traverse(root.right) + ')'

            left = ''
            if root.left is not None:
                left = '(' + print_traverse(root.left) + ')'
            elif len(right) > 0:
                left = '()'
            
            print_value = left+right
            if len(print_value) > 0:
                print_value = f"{print_value}"
            
            return f"{root.val}{print_value}"
        
        return print_traverse(root)
