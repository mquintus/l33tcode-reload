# 1123 - Lowest Common Ancestor of Deepest Leaves
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        maxdepth = 0
        ca = root
        ca_depth = float('inf')

        def solve(node, depth):
            nonlocal ca, maxdepth
            if node.left is None and node.right is None:
                #print("Child node", node.val, "of depth", depth, f"and maxdepth:{maxdepth} ca:{ca.val} ")
                # this is a child node
                if maxdepth < depth:
                    maxdepth = depth
                    ca = node
                return depth

            depth_left = -1
            depth_right = -1
            if node.left is not None:
                depth_left = solve(node.left, depth+1)
            if node.right is not None:
                depth_right = solve(node.right, depth+1)
            if depth_right == maxdepth and depth_left == maxdepth:
                #print("has_deepest_left and has_deepest_right:",node.val)
                ca = node
#                ca_depth
            return max(depth_left, depth_right)

        
        solve(root, 0)
        return ca
