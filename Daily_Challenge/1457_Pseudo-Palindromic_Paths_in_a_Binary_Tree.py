# 1457 - Pseudo-Palindromic Paths in a Binary Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # The obvious answer is that 
        # if all number counts are even and at most one is odd, it can be rearranged
        # To be palindromic
        def check(prefix_counter):
            uneven = False
            possible = True
            for c in prefix_counter:
                if c % 2 == 1 and uneven == False:
                    uneven = True
                elif c % 2 == 1:
                    possible = False
                    break
            return possible
                    

        def get_subpaths(node, prefix_counter):
            if node is None:
                return 0
            
            prefix_counter[node.val] += 1

            ret = 0
            if node.left is None and node.right is None:
                # only leaf nodes
                if check(prefix_counter):
                    ret = 1
            else:
                ret = get_subpaths(node.left, prefix_counter)
                ret += get_subpaths(node.right, prefix_counter)

            prefix_counter[node.val] -= 1

            return ret

        return get_subpaths(root, [0] * 10)


