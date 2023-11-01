# 501 - Find Mode in Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        maxCount = 0
        hashMap = {}

        children = [root]
        while len(children) > 0:
            child = children.pop()
            if child is None:
                continue

            val = child.val
            if val not in hashMap:
                hashMap[val] = 0
            hashMap[val] += 1

            if hashMap[val] > maxCount:
                maxCount = hashMap[val]

            children.append(child.left)
            children.append(child.right)
        
        results = []
        for k,v in hashMap.items():
            if v == maxCount:
                results.append(k)

        return results
