# 513 - Find Bottom Left Tree Value
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        states = [[root, 0]]
        deepest_node = root.val
        deepest_level = 0
        while states:
            root, depth = states.pop(0)
            if depth > deepest_level:
                deepest_level = depth
                deepest_node = root.val
            if root.left is not None:
                states.append([root.left, depth + 1])
            if root.right is not None:
                states.append([root.right, depth + 1])
        return deepest_node
