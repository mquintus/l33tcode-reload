# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        prevNode = ListNode(next=head)
        prevHead = prevNode
        beforeReversedListNode = prevHead
        i = 1

        if left == right:
            return head
        
        while curr is not None:
            nextNode = curr.next

            if i == left - 1:
                beforeReversedListNode = curr
            if i == left:
                reversedListEnd = curr
                reversedListStart = curr
            if i > left and i <= right:
                curr.next = reversedListStart
                reversedListStart = curr
            if i == right:
                beforeReversedListNode.next = reversedListStart
                reversedListEnd.next = nextNode
                break

            curr = nextNode
            i += 1

        return prevHead.next



        
