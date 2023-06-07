'''
First approach: Build a tree, reading from the right.
'''
class Node:
    left = None
    right = None
    operator = None
    def solve(self):
        if self.operator == '+':
            return self.left.value + self.right.value
        if self.operator == '-':
            return self.left.value - self.right.value
        if self.operator == '/':
            return self.left.value / self.right.value
        if self.operator == '*':
            return self.left.value * self.right.value

operators = ['-', '+', '*', '/']

def create_tree(tokens: List[str]) -> Node:
    tree_root = Node()
    op = tokens.pop()
    if op not in operators:
        tree_root.operator = '='
        tree_root.value = int(op)
        return tree_root
    else:
        node = Node()
        node.operator = op
        node.right = create_tree(tokens)
        node.left = create_tree(tokens)
        node.value = int(node.solve())
        return node
      
class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
      root_node = create_tree(tokens)
      return root_node.value
