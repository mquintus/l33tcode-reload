# 2196 - Create Binary Tree From Descriptions
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        hashmap = {}
        hasparent = set()
        isparent = set()
        for parent, child, isLeft in descriptions:
            if child not in hashmap:
                hashmap[child] = TreeNode(child)
            hasparent.add(child)

            if parent not in hashmap:
                hashmap[parent] = TreeNode(parent)
            isparent.add(parent)
            if isLeft:
                hashmap[parent].left = hashmap[child]
            else:
                hashmap[parent].right = hashmap[child]
        
        for node in isparent:
            if node not in hasparent: 
                break        
                
        return hashmap[node]
