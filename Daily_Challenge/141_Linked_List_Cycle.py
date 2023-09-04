# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        while slow is not None and head is not None:
            head = head.next
            if head is None:
                return False
            if slow == head:
                return True
            head = head.next
            slow = slow.next
        return False
        
