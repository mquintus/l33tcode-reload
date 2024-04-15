# 129 - Sum Root to Leaf Numbers
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        result = 0
        currSum = 0

        def recursion(root, currSum):
            if root.left is None and root.right is None:
                currSum *= 10
                currSum += root.val
                #print(root.val, currSum)
                return currSum
            
            bufSum = 0
            if root.left is not None:
                bufSum += recursion(root.left, currSum * 10 + root.val)
            if root.right is not None:
                bufSum += recursion(root.right, currSum * 10 + root.val)

            return bufSum 
                
        
        return recursion(root, 0)



