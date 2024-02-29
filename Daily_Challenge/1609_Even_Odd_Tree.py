# 1609 - Even Odd Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        states = [[root, 0]]
        odd = 1
        levelmin = root.val
        prev_d = -1
        while states:
            root, depth = states.pop(0)
            print(root.val, depth+odd, root.val % 2, (odd+depth) % 2)
            if root.val % 2 != (odd+depth) % 2:
                #print(root.val)
                return False

            if prev_d < depth:
                levelmin = root.val
                prev_d = depth
            else:
                if (depth % 2 == odd):
                    if (root.val >= levelmin):
                        return False
                    else:
                        print(depth, odd, root.val, levelmin)
                if (depth % 2 != odd):
                    if root.val <= levelmin:
                        return False
                    else:
                        print(depth, odd, root.val, levelmin)
            levelmin = root.val
                
            if root.left is not None:
                states.append([root.left, depth + 1])
            if root.right is not None:
                states.append([root.right, depth + 1])
        return True
