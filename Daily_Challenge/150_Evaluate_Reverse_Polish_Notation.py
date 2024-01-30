# 150 - Evaluate Reverse Polish Notation
'''
First approach: Build a tree, reading from the right.
Second approach: Use a stack, reading from the left.
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


'''Second approach: Use a stack, reading from the left.'''
def stack_solution(tokens: List[str]) -> int:
    def solve(b,a,op):
        #print(b,a,op)
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            return a / b


    myStack = []
    while len(tokens) > 0:
        el = tokens.pop(0)
        if el in operators:
            value = solve(myStack.pop(), myStack.pop(), el)
        else:
            value = el
        myStack.append(int(value))
    return myStack.pop()

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #root_node = create_tree(tokens)
        #return root_node.value
        return stack_solution(tokens)


