# 2641 - Cousins in Binary Tree II
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = []
        def cb_first(left, rv, depth):
            while len(levels) <= depth: 
                levels.append(0)
            levels[depth] += left.val
            #if right is not None:
            #    levels[depth] += right.val

        def cb_second(left, rv, depth):
            prev = left.val
            left.val = levels[depth] - left.val
            left.val -= rv
            #print(prev, left.val, '(',levels[depth], rv,')')

        def rec(node, depth, cb):
            if node is None: return
            rv = 0
            lv = 0
            if node.right is not None:
                rv = node.right.val
            if node.left is not None:
                lv = node.left.val
                cb(node.left, rv, depth)
            if node.right is not None:
                cb(node.right, lv, depth)
            if node.right is not None:
                rec(node.right, depth+1, cb)
            if node.left is not None:
                rec(node.left, depth+1, cb)

        root.val = 0
        rec(root,0,cb_first)
        #print(levels)
        rec(root,0,cb_second)
        return root
