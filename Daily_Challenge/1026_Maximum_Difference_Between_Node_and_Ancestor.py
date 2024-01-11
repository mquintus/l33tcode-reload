# 1026 - Maximum Difference Between Node and Ancestor
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        
        
        def get_smallest_child_and_biggest_child_and_biggest_difference(root) -> [int, int]:
            if root is None:
                return float('inf'), float('-inf'), float('-inf')
            if root.left is None and root.right is None:
                return root.val, root.val, float('-inf')

            scl, bcl, bdl = get_smallest_child_and_biggest_child_and_biggest_difference(root.left)
            scr, bcr, bdr = get_smallest_child_and_biggest_child_and_biggest_difference(root.right)

            smallest_child = min(scl, scr)
            biggest_child = max(bcl, bcr)
            biggest_difference = max(bdl, bdr)

            current_difference = max(abs(root.val - smallest_child), abs(root.val - biggest_child))
            biggest_difference = max(biggest_difference, current_difference)
            
            smallest_child = min(root.val, smallest_child)
            biggest_child = max(root.val, biggest_child)
            return smallest_child, biggest_child, biggest_difference

        _, _, biggest_difference = get_smallest_child_and_biggest_child_and_biggest_difference(root)  
        return biggest_difference
