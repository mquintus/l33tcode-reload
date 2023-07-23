# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import functools

class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        '''
        Return a list of all possible full binary trees with n nodes.

        I will not consider symmetry for the moment.

        But we can already say that the number of nodes in a balanced tree has to be uneven/odd.
        If n % 2 == 0:
            return []

        Let's try a recursive approach:
        First we are at the root node.
        If n == 1:
            # we stop here.
            return [TreeNode()]

        From the root nodes perspective, all options are to give the left node or the right node any
        even number of children.

        solutions = []
        depth = 0
        for left in range(0, n, 2)
            right = n - left

            cur_solution = [TreeNode()]

            left_nodes = solve(left)
            right_nodes = solve(right)

            cur_solution.append(left_nodes)
            cur_solution.append(right_nodes)

            solutions.append(cur_solution)
        '''
        if n == 1:
            return [TreeNode()]

        if n % 2 == 0:
            return []

        @cache
        def solve(n: int):
            if n == 0:
                return [TreeNode()]
            
            n -= 2

            solutions = []
            for left in range(0, n + 1, 2):
                right = n - left

                for left_branch in solve(left):
                    for right_branch in solve(right):
                        root = TreeNode(0, left_branch, right_branch)
                        solutions.append(root)
            return solutions


        return solve(n - 1)

