# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:

        dp = [[None for _ in range(n + 1)] for _ in range(n + 1)]

        def solve(left, right):
            if left > right:
                return [None]
            if dp[left][right] is not None:
                return dp[left][right]

            allTrees = []
            for i in range(left, right + 1):
                for r in solve(i + 1, right):
                    for l in solve(left, i - 1): 
                        root = TreeNode(
                                i,
                                l,
                                r
                        )
                        allTrees.append(root)
            return allTrees

        return solve(1, n)
