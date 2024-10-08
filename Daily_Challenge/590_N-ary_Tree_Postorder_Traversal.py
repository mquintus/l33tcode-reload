# 590 - N-ary Tree Postorder Traversal
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = []
        stack.append((root,False))
        solution = []
        while stack:
            node,visited = stack.pop()
            if node is None:
                continue
            if visited:
                solution.append(node.val)
                continue
            stack.append((node, True))
            for child in node.children[::-1]:
                stack.append((child,False))
            
        return solution
