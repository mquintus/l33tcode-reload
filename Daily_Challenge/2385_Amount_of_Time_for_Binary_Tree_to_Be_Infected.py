# 2385 - Amount of Time for Binary Tree to Be Infected
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.infected = root
        def add_head(root, up):
            if root.left is not None:
                root.left.upRight = None
                root.left.upLeft = root
                add_head(root.left, root)
    
            if root.right is not None:
                root.right.upLeft = None
                root.right.upRight = root
                add_head(root.right, root)

            if root.val == start:
                self.infected = root

        root.upLeft = None
        if root.left is not None:
            root.left.upLeft = root
            root.left.upRight = None
            add_head(root.left, root)

        root.upRight = None
        if root.right is not None:
            root.right.upRight = root
            root.right.upLeft = None
            add_head(root.right, root)

        self.max_distamce = 0
        def dfs(root, distance, orig='null'):
            if root is None:
                return
            
            #print(root.val, distance)
            self.max_distamce = max(self.max_distamce, distance)
            
            if orig != 'left':
                dfs(root.left, distance + 1, orig='upLeft')
            if orig != 'upLeft':
                dfs(root.upLeft, distance + 1, orig='left')
            if orig != 'upRight':
                dfs(root.upRight, distance + 1, orig='right')
            if orig != 'right':
                dfs(root.right, distance + 1, orig='upRight')
            
        #print(self.infected)
        dfs(self.infected, 0)

        return self.max_distamce

