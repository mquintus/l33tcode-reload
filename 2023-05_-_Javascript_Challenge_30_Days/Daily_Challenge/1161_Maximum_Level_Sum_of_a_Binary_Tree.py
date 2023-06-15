# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        '''
        This challenge ignores the tree structure somewhat and
        want to aggregate all nodes of a tree level, even if they are in different
        subtrees.

        If this is to be solved using only tree traversal methods,
        it would be easiest to return an array of depth + sum from each child
        and add values from both childs up, grouped by depth.
        
        The returned data structure can be simplyfied to a list.

        '''
        #if root is None:
            #return -1

        def helper(root) -> list:
            returnList = [root.val]
            leftValues = []
            rightValues = []
            if root.left is not None:
                leftValues = helper(root.left) 
            if root.right is not None:
                rightValues = helper(root.right) 

            for i in range(max(len(leftValues), len(rightValues))):
                if i >= len(leftValues):
                    level_val = rightValues[i]
                elif i >= len(rightValues):
                    level_val = leftValues[i]
                else:
                    level_val = sum([leftValues[i], rightValues[i]])
                returnList.append(level_val)

            return returnList

        all_levels = helper(root)
        print(all_levels)
        max_val = all_levels[0]
        max_pos = 0
        for level in range(len(all_levels)):
            if max_val < all_levels[level]:
                max_val = all_levels[level]
                max_pos = level
        return max_pos + 1
