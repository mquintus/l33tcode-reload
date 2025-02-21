# 1261 - Find Elements in a Contaminated Binary Tree
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.values = set()
        root.val = 0
        def rec(treeNode):
            self.values.add(treeNode.val)
            if treeNode.left is not None:
                treeNode.left.val = 2 * treeNode.val + 1
                rec(treeNode.left)
            if treeNode.right is not None:
                treeNode.right.val = 2 * treeNode.val + 2
                rec(treeNode.right)
        rec(root)
        #print(self.values)

    def find(self, target: int) -> bool:
        return target in self.values        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
