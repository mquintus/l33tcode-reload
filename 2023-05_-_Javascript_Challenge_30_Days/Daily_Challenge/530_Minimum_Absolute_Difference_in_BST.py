# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        '''
        Luckily a "binary search tree" has the property that it is sorted.
        This knowledge makes this question easy to solve: Just iterate
        the tree in the correct order an compare a node with the following node.
        '''
        def next(root) -> Optional[TreeNode]:
            if root.left is not None:
                for node in next(root.left):
                    yield node
            yield root
            if root.right is not None:
                for node in next(root.right):
                    yield node
        
        prev = None
        min_distance = None
        for node in next(root):
            print(node.val)
            if prev is None:
                prev = node
                continue
            if min_distance is None:
                min_distance = node.val - prev.val
            min_distance = min(min_distance, node.val - prev.val)
            prev = node
        return min_distance
            
'''
[4,2,6,1,3]
[1,0,48,null,null,12,49]
[8,0,48,null,null,12,100]
[30,0,750,null,null,500,1000,100,null,null,2000]
[130,100,750,null,null,500,1000,200,null,null,2000,160,400,null,3000,null,175]
'''
