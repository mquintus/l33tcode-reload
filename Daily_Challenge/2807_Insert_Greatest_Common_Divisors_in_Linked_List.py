# 2807 - Insert Greatest Common Divisors in Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev = node
        node = node.next
        while node:
            newNode = ListNode(
                 math.gcd(node.val, prev.val),
                 node
            )
            prev.next = newNode
            prev = node
            node = node.next
        return head
