# 2816 - Double a Number Represented as a Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def doubleNext(head) -> int:
            overflow = 0 
            if head is None:
                return 0
            head.val *= 2
            head.val += doubleNext(head.next)
            if head.val > 9:
                head.val -= 10
                overflow = 1
            return overflow

        overflow = doubleNext(head)
        newHead = head
        if overflow == 1:
            newHead = ListNode(
                1, head)
        return newHead
