"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_register = [None for _ in range(1001)]

        index = 0
        curr = head
        while curr is not None:
            node_register[index] = Node(curr.val)
            if index > 0:
                node_register[index - 1].next = node_register[index]
            curr.index = index
            curr = curr.next
            index += 1

        index = 0
        curr = head
        while curr is not None:
            if curr.random is not None:
                old_random_node_of_curr = curr.random
                index_of_random_node = old_random_node_of_curr.index
                node_register[index].random = node_register[index_of_random_node]
            curr = curr.next
            index += 1

        return node_register[0]
