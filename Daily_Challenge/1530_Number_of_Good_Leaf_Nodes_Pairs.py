# 1530 - Number of Good Leaf Nodes Pairs
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        counter = 0
        def rec(node):
            if node is None:
                return []
            #print("Node:", node.val)
            distances = []

            d1 = []
            d2 = []
            if node.left is not None:
                d1 = rec(node.left)
                for i in range(len(d1)):
                    d1[i] += 1
            if node.right is not None:
                d2 = rec(node.right)
                for i in range(len(d2)):
                    d2[i] += 1
            if node.left is None and node.right is None:
                # leaf node :-)
                distances = [0]

            for p1 in d1:
                for p2 in d2:
                    #print("Dist", p1, p2, p1 + p2 >= distance)
                    if p1 + p2 <= distance:
                        nonlocal counter
                        counter += 1
            
            distances += d1
            distances += d2
            return distances
        rec(root)
        return counter
