# 1028 - Recover a Tree From Preorder Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def count_dashes(i):
            c = 0
            while i < len(traversal) and traversal[i] == '-':
                c += 1
                i += 1
            return i, c

        def get_number(i):
            number = ""
            while i < len(traversal) and traversal[i] != '-':
                number += traversal[i]
                i += 1
            return i, int(number)

        def rec(node, parent, i, depth):
            if i == len(traversal):
                return i, -1
            
            i,c = count_dashes(i)

            if c == depth:
                i,el = get_number(i)
                left_node = TreeNode(el)
                node.left = left_node
                i, right_depth = rec(left_node, node, i, depth+1)
                if right_depth == depth:
                    i,el = get_number(i)
                    right_node = TreeNode(el)
                    node.right = right_node
                    return rec(right_node, node, i, depth+1)
                else:
                    return i, right_depth

            return i, c

        i,el = get_number(0)
        root = TreeNode(el)
        rec(root, None, i, 1)
        return root
