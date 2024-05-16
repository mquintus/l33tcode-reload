# 2331 - Evaluate Boolean Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def evaluate(node):
            if node.val == 0:
                return False
            if node.val == 1:
                return True

            my_operator = operator.__or__ if node.val == 2 else operator.__and__
            return my_operator(evaluate(node.left), evaluate(node.right))

        return evaluate(root)
