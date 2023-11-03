# 2265 - Count Nodes Equal to Average of Subtree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def get_subtree_sum_and_count(root):
            if root is None:
                return 0,0,0

            st_sum = root.val
            st_count = 1

            a1, b1, c1 = get_subtree_sum_and_count(root.left)
            a2, b2, c2 = get_subtree_sum_and_count(root.right)

            st_sum += a1 + a2
            st_count += b1 + b2

            counter = c1 + c2
            avg = st_sum // st_count
            if avg == root.val:
                counter += 1
            #print(st_sum, st_count, avg, root.val, counter)

            return st_sum, st_count, counter

        _, _, counter = get_subtree_sum_and_count(root)
        return counter

