# 2096 - Step-By-Step Directions From a Binary Tree Node to Another
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # When going from node a or node b to the root,
        # those two paths (from node to root) intersect
        # at the point where
        # the shortest path from a node to another node is. 
        # 

        # Therefore we search for both nodes
        # and then find there the nodes intersect.

        # Finally, the part of the path to node a 
        # must go up instead of down.
        def findNodePath(currnode, targets, steps, rootpaths):
            if currnode is None:
                return rootpaths
            if currnode.val in targets:
                rootpaths[currnode.val] = [*steps]
                targets.remove(currnode.val)
            if len(targets) == 0:
                return rootpaths
            if currnode.left is not None:
                steps.append("L")
                rootpaths = findNodePath(currnode.left, targets, steps, rootpaths)
                steps.pop()
            if currnode.right is not None:
                steps.append("R")
                rootpaths = findNodePath(currnode.right, targets, steps, rootpaths)
                steps.pop()
            return rootpaths
        
        rootpaths = findNodePath(currnode=root, targets=set([startValue, destValue]), steps=[], rootpaths={})
        #print(rootpaths)

        i = 0
        while i < min([len(rootpaths[startValue]), len(rootpaths[destValue])]):
            #print(i, rootpaths[startValue][i], rootpaths[destValue][i])
            if rootpaths[startValue][i] != rootpaths[destValue][i]:
                #print(i)
                break
            i += 1
        rootpaths[startValue] = rootpaths[startValue][i:]
        rootpaths[destValue] = rootpaths[destValue][i:]
        
        # From startValue to intersection, just go up.
        return "".join(['U'] * len(rootpaths[startValue]) + rootpaths[destValue] )
        



