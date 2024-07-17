# 1110 - Delete Nodes And Return Forest
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def populateForest(root, isroot, forest):
            # Returns if this root is deleted.
            nonlocal to_delete
            if root is None:
                return True
            
            deletethis = root.val in to_delete
            if isroot and not deletethis:
                forest.append(root)

            childIsRoot = False
            if deletethis:
                childIsRoot = True

            deleteLeft = populateForest(root.left, childIsRoot, forest)
            if deleteLeft:
                root.left = None
            
            deleteRight = populateForest(root.right, childIsRoot, forest)        
            if deleteRight:
                root.right = None

            return deletethis
            
        forest = []
        populateForest(root, True, forest)
        return forest

            
