# 515 - Find Largest Value in Each Tree Row
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        answer = []
        def dfs(node, level):
            if len(answer) <= level:
                answer.append(float(-inf))
            answer[level] = max(answer[level], node.val)
            for n2 in [node.left, node.right]:
                if n2 is not None:
                    dfs(n2, level+1)

        dfs(root,0)
        return answer
            
