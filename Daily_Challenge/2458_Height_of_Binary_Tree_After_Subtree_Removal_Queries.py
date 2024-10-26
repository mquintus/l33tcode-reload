# 2458 - Height of Binary Tree After Subtree Removal Queries
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        fromTop = [0 for _ in range(int(10e5)+1)]
        fromBottom = [0 for _ in range(int(10e5)+1)]
        levels = [[]]
        def getLevel(node, height):
            if node is None: return height-1
            if len(levels) <= height: levels.append([])
            fromTop[node.val] = height
            depthLeft = getLevel(node.left, height+1)
            depthRight = getLevel(node.right, height+1)
            maxDepth = max(depthLeft,depthRight)
            fromBottom[node.val] = maxDepth
            if len(levels[height]) == 0:
                levels[height].append(maxDepth)
            elif len(levels[height]) == 2 and maxDepth > levels[height][1]:
                levels[height].pop(0)
                levels[height].append(maxDepth)
            elif len(levels[height]) == 2 and maxDepth > levels[height][0]:
                levels[height].pop(0)
                levels[height].insert(0,maxDepth)
            elif len(levels[height]) < 2 and maxDepth > levels[height][0]:
                levels[height].append(maxDepth)
            elif len(levels[height]) < 2 and maxDepth <= levels[height][0]:
                levels[height].insert(0, maxDepth)
            return maxDepth
        getLevel(root, 0)

        ans = []
        for query in queries:
            lvl = fromTop[query]
            depth_curr = fromBottom[query]
            if len(levels[lvl]) == 2:
                depth_low, depth_high = levels[lvl]
            else:
                depth_low, depth_high = -1, levels[lvl][0]
            #print("Query:",query,"is on level",lvl,"with own depth",depth_curr,"and the levels deepest paths are",depth_low, "and",depth_high)

            if depth_curr == depth_high:
                #print("Removing deepest, return lvl-1 or next deepest",lvl-1, depth_low)
                ans.append(max(lvl-1, depth_low))
            else:
                #print("Removing not deepest, maintain deepest",depth_high," of level",lvl)
                ans.append(depth_high)
            
        return ans




